let view_meetup = document.querySelector('.meetup-modal');
let error_message = document.querySelector('.error-message');
let add_meetup = document.querySelector('.created-meetups');
let add_question = document.querySelector('.append-items');
let meetup_template = '';
let new_meetup = '';
let all_meetup = '';
let comment_str = '';
let questionItem = null

let meetup_item = []


fetch('http://127.0.0.1:5000/api/v2/meetups',{
    method: 'GET',
    headers: {
        'Authorization': `Bearer ${localStorage['currentuser']}`,
        'content-Type':'application/json'
    },
})
.then(response => response.json())
.then(data => {
    let string = "";
    let object = data;
    for (let message in object) {
        string += object[message];
    }
    if(string == 'Token is invalid'){
        window.location = "file:///home/wekesa/Desktop/Questioner-gh-pages/UI/routes/user.html";
    }
    for(let item in object){
        object[item].forEach(element => {
            meetup_item.push(element['id']);
            all_meetup =`
                <div class="user">
                    <div class="date-holder">
                        <div class="meetup-image">
                            <img src="${element['images']}" alt="myimage" class="meet-up-image">
                        </div>
                        <div class="meetup-date-holder">
                            <p>posted on ${element['createdon']}</p>
                        </div>
                    </div>
                    <div class="meetup-title-holder"><p>${element['id']}: ${element['topic']}</p></div>
                    <div class="meetup-details"><p>Happening at ${element['location']} on <span>${element['happeningon']}</span></p></div>
                    <div class="meetup-details">
                        <i class="fa fa-tag" aria-hidden="true">${element['tags']}</i>
                    </div>
                    <div class="delete-holder ">
                        <div class="btn-one"><button class="delete view-qs" onClick="getMeetupInfo(${element['id']});">View Questions</button></div>
                        <div class="btn-two"><button class="delete" onClick="deleteData(${element['id']});">Delete</button></div>                            
                    </div>
                </div>
                `
                add_meetup.insertAdjacentHTML("afterbegin", all_meetup)
        });
 
    }
    
})
.catch(error => console.log('bad request', error))

function submitMeetupInfo(){
    const url = 'http://127.0.0.1:5000/api/v2/meetups';
    let form = document.forms['meetupform'];
    let formData = new FormData(form);
    let data = {};
    for (let [key, prop] of formData){
        data[key] = prop;
    }
    VALUE = JSON.stringify(data);
    fetch(url,{
        method: 'POST',
        headers: {
            'Authorization': `Bearer ${localStorage['currentuser']}`,
            'content-Type':'application/json'
        },
        body: VALUE
    })
    .then(response => response.json())
    .then(data => {
        let string = "";
        let object = data;
        for (let message in object) {
            string += object[message];
        }
        if(string == 'Token is invalid' || string == 'Permission denied!'){
            window.location = "file:///home/wekesa/Desktop/Questioner-gh-pages/UI/routes/user.html";
        }
        else if(string == 'tags is missing a value' || string == 'happeningOn is missing a value' || string == 'topic is missing a value'
                            || string == 'images is missing a value' || string == 'location is missing a value' || string == 'image URL is not valid'
                            || string == 'date should be in the format yyyy-mm-dd' || string == 'Another meetup is happening on the same location!'
                            || string == 'Another meetup has the same topic!'){
            
            meetup_template +=`
                <p>${string}</p>
            `
            error_message.innerHTML=" "
            error_message.insertAdjacentHTML("afterbegin", meetup_template)
            
        }
        else{
            new_meetup = `
                <div class="user">
                    <div class="date-holder">
                        <div class="meetup-image">
                            <img src="${data['images']}" alt="myimage" class="meet-up-image">
                        </div>
                        <div class="meetup-date-holder">
                            <p>posted on ${data['createdon']}</p>
                        </div>
                    </div>
                    <div class="meetup-title-holder"><h3>${data['topic']}</h3></div>
                    <div class="meetup-details"><p>Happening at ${data['location']} on <span>${data['happeningon']}</span></p></div>
                    <div class="meetup-details">
                        <i class="fa fa-tag" aria-hidden="true">${data['tags']}</i>
                    </div>
                    <div class="delete-holder ">
                        <div class="btn-one"><button class="delete view-qs">View Questions</button></div>
                        <div class="btn-two"><button class="delete">Delete</button></div>                            
                    </div>
                </div>
                `
            add_meetup.insertAdjacentHTML("afterbegin", new_meetup);
            meetup_template +=`
                <p>Meetup successfully created!</p>
            `
            error_message.innerHTML=" "
            error_message.insertAdjacentHTML("afterbegin", meetup_template)
        }
    })
    .catch(error => console.log('bad request', error))
}