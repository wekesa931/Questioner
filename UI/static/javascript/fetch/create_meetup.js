//let meetup = document.querySelector('.meetup-form');
let view_meetup = document.querySelector('.meetup-modal');
let error_message = document.querySelector('.error-message');
let add_meetup = document.querySelector('.created-meetups');
let add_question = document.querySelector('.append-items');
//const inpt = document.querySelector('.modal-question-input');
let meetup_template = '';
let new_meetup = '';
let all_meetup = '';
let comment_str = '';
let questionItem = null

fetch('https://questionerapplication.herokuapp.com/api/v2/meetups',{
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
        window.location = "https://wekesa931.github.io/Questioner/UI/routes/user.html";
    }
    for(let item in object){
        object[item].forEach(element => {
            all_meetup =`
                <div class="user">
                    <div class="date-holder">
                        <div class="meetup-image">
                            <img src="${element['images']}" alt="myimage" class="meet-up-image">
                        </div>
                        <div class="meetup-date-holder">
                            <p>Posted on ${element['createdon'].split(' ', 4).join(' ')}</p>
                        </div>
                    </div>
                    <div class="meetup-title-holder"><p>${element['topic']}</p></div>
                    <div class="meetup-details"><p>Happening at <b>${element['location']}</b> on <span>${element['happeningon'].split(' ', 4).join(' ')} at <b>${element['happeningat']}</b></span></p></div>
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
    const url = 'https://questionerapplication.herokuapp.com/api/v2/meetups';
    let form = document.forms['meetupform'];
    let formData = new FormData(form);
    let data = {};
    for (let [key, prop] of formData){
        data[key] = prop;
    }
    VALUE = JSON.stringify(data);
    console.log(VALUE)
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
            window.location = "https://wekesa931.github.io/Questioner/UI/routes/user.html";
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
            console.log(data['id']);
            new_meetup = `
                <div class="user">
                    <div class="date-holder">
                        <div class="meetup-image">
                            <img src="${data['images']}" alt="myimage" class="meet-up-image">
                        </div>
                        <div class="meetup-date-holder">
                            <p>posted on ${data['createdon'].split(' ', 4).join(' ')}</p>
                        </div>
                    </div>
                    <div class="meetup-title-holder"><p>${data['topic']}</p></div>
                    <div class="meetup-details"><p>Happening at <b>${data['location']}</b> on <span>${data['happeningon'].split(' ', 4).join(' ')} at <b>${data['happeningat']}</b></span></p></div>
                    <div class="meetup-details">
                        <i class="fa fa-tag" aria-hidden="true">${data['tags']}</i>
                    </div>
                    <div class="delete-holder ">
                        <div class="btn-one"><button class="delete view-qs" onClick="getMeetupInfo(${data['id']});">View Questions</button></div>
                        <div class="btn-two"><button class="delete" onClick="deleteData(${data['id']});">Delete</button></div>                            
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

function deleteData(meetup_id){
    let del_url ='https://questionerapplication.herokuapp.com/api/v2/meetups/';
    fetch(del_url + meetup_id,{
        method: 'DELETE',
        headers: {
            'Authorization': `Bearer ${localStorage['currentuser']}`,
            'content-Type':'application/json'
        }
    })
    .then(response => response.json())
    .then(data => {
        let string = "";
        let object = data;
        for (let message in object) {
            string += object[message];
        }
        if(string == 'Token is invalid' || string == 'Permission denied!'){
            window.location = "https://wekesa931.github.io/Questioner/UI/routes/user.html";
        }
        else if(string == 'meetup deleted successfully!'){
            location.reload();
            meetup_template +=`
                <p>${string}</p>
            `
            error_message.innerHTML=" "
            error_message.insertAdjacentHTML("afterbegin", meetup_template)

        }
    })

}

function getMeetupInfo(meetup_id){
    view_meetup.classList.toggle('modal-hide');
    mtp_url = 'https://questionerapplication.herokuapp.com/api/v2/meetups/';
    fetch(mtp_url + meetup_id,{
    method: 'GET',
    headers: {
        'Authorization': `Bearer ${localStorage['currentuser']}`,
        'content-Type':'application/json'
    },
})
.then(response => response.json())
.then(data =>
    {
    let qsn_string = "";
    let string = "";
    let object = data;
    questions = object['questions'];
    string =`
        <i class="fa fa-window-close" aria-hidden="true" onclick="closeWindow();"></i>
        <div class="modal-meetup-item">
            <div class="modal-user">
                <div class="modal-date-holder">
                    <div class="modal-meetup-image">
                        <img src="${object['images']}" alt="myimage" class="meet-up-image">
                    </div>
                    <div class="modal-meetup-date-holder">
                        <p>Posted on ${object['createdon'].split(' ', 4).join(' ')}</p>
                    </div>
                </div>
                <div class="modal-meetup-title-holder"><p>${object['topic']}</p></div>
                <div class="modal-meetup-details"><p>Happening at <b>${object['location']}</b> on <span>${object['happeningon'].split(' ', 4).join(' ')} at <b>${object['happeningat']}</span></p></div>
                <div class="modal-meetup-details">
                    <i class="fa fa-tag" aria-hidden="true">${object['tags']}</i>
                    <div id="modal-btn-input">
                        <input type="button" value="Post Question" class="modal-post-question" id="question-button" onClick="postQuestion();" style="width: 100%;padding: 4%;">
                    </div> 
                </div>
            </div>
        </div>
        <div class="modal-question-input modal-hide">
            <div class="modal-comment">
                <form name="questionform" method="POST">
                    <input type="text" name="title" id="title-holder" placeholder="Title" required>
                    <br><br>
                    <textarea name="body" placeholder="Post Question"></textarea>
                </form>
            </div>
            <div class="modal-sub-btn">
                    <input type="button" value="Post Question" class="modal-post-question" onclick="submitQuestionInfo(${object['id']});" style="width: 18%;padding: 1%;">
            </div> 
        </div>
    `
    view_meetup.insertAdjacentHTML("afterbegin", string)
    
    for(let item in questions){
        let votes_holder=0;
        votes_holder +=1;
        questionItem = questions[item]
        votes =null;
        qsn_string = `
            <div class="modal-user modal-question-item-holder">
                <div class="modal-meetup-title-holder"><h3></h3></div>
                <div class="modal-date-holder">Posted on ${questionItem['createdon']} BY:&nbsp;&nbsp;<b>${questionItem['firstname']} ${questionItem['lastname']}</b></div>
                <div class="modal-meetup-details">
                    <p>
                        ${questionItem['title']}
                    </p>
                    <p>
                        ${questionItem['body']}
                    </p>
                </div>
                <div class="modal-comment${questionItem['qsn_id']}">
                    <form name="commentform${questionItem['qsn_id']}" method="POST">
                        <textarea name="comment" placeholder="Post Comment"></textarea>
                        <div class="modal-sub-btn">
                            <input type="button" value="Post Comment" class="modal-post-question" onclick="submitCommentInfo(${questionItem['qsn_id']});">
                        </div>  
                    </form>
                </div>
                        
                <div class="modal-vote modal-vote${questionItem['qsn_id']}">
                    <i class="fa fa-thumbs-up" onclick="upvoteInfo(${questionItem['qsn_id']})"></i>
                        <div class="votes-holder votes-holder${questionItem['qsn_id']}">
                            ${questionItem['votes']}                        
                        </div>
                    <i class="fa fa-thumbs-down" onclick="downvoteInfo(${questionItem['qsn_id']})"></i>
                </div>
                <div class="com-item modal-comment-statements${questionItem['qsn_id']}"></div>
            </div>
        `
        add_question.insertAdjacentHTML('afterbegin',qsn_string)
    
        let comment_piece = document.querySelector(`.modal-comment-statements${questionItem['qsn_id']}`);
        comment_items = questionItem['comments']
        comment_items.forEach(element =>{
            let comment_str = `
                    <p class="comment-text">
                        ${element[0]}
                        <span><b>- ${element[1]}  ${element[2]}</b></span>
                    </p>             
                `
                comment_piece.insertAdjacentHTML("beforeend", comment_str)
        })
    }
    
    if(string == 'Token is invalid'){
        window.location = "https://wekesa931.github.io/Questioner/UI/routes/user.html";
    }  
})
.catch(error => console.log('bad request', error))
}
function postQuestion(){   
    let inpt = document.querySelector('.modal-question-input');
    inpt.classList.toggle('modal-hide');
 }
function closeWindow(){
    //let modalItem = document.querySelector('.meetup-modal');
    window.location.reload()
}
function logOut(){
    localStorage.clear();
    window.location = "../routes/user.html";
}
fetch('https://questionerapplication.herokuapp.com/api/v2/user/name',{
    method: 'GET',
    headers: {
        'Authorization': `Bearer ${localStorage['currentuser']}`,
        'content-Type':'application/json'
    }
})
.then(response => response.json())
.then(data => {
    let string = "";
    let object = data;
    for (let message in object) {
        string += object[message];
    }
    if(string == 'Token is invalid'){
        window.location = "https://wekesa931.github.io/Questioner/UI/routes/user.html";
    }
        let user_person =`
                <p class="full-profile" style="text-transform: capitalize;">${object['firstname']} ${object['lastname']}</p>         
            `
            let user_item = document.querySelector('#admin-user')
            user_item.insertAdjacentHTML("afterbegin",user_person)
    
})
.catch(error => console.log('bad request', error))