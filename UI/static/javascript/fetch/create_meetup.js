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