let chan_psw = document.querySelector('.chan-psw');
let change_pass = document.querySelector('.change-full-profile');
let user_meetupList = document.querySelector('.user-meetups-display');
fetch('https://questionerapplication.herokuapp.com/api/v2/meetups',{
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
        window.location = "../../routes/user.html";
    }
    for(let item in object){
        object[item].forEach(element => {
            //meetup_item.push(element['id']);
            let all_meetup =`
                <div id="qsn_item">
                    <div class="user user${element['id']}">
                        <div class="date-holder">
                            <div class="meetup-image">
                                <img src="${element['images']}" alt="myimage" class="meet-up-image">
                            </div>
                            <div class="meetup-date-holder">
                                <p>posted on ${element['createdon'].split(' ', 4).join(' ')}</p>
                            </div>
                        </div>
                            <div class="meetup-title-holder"><p>${element['topic']}</p></div>
                            <div class="meetup-details"><p>Happening at <b>${element['location']}</b> on <span>${element['happeningon'].split(' ', 4).join(' ')} at <b>${element['happeningat']}</b></span></p></div>
                                <div class="meetup-details">
                                    <i class="fa fa-tag" aria-hidden="true">${element['tags']}</i>
                                </div>
                        <div class="delete-holder delete-holder${element['id']}">
                            <p>RSVP</p>
                                <div class="btn-one btn-one${element['id']}">
                                    <div class="btn-holer btn-holer${element['id']}">
                                        <form name="atendform" method="POST">
                                            <input type="text" name="status" value="YES" class="hide" required>
                                            <button type="button" class="delete maybe rsvp" onclick="attendRsvp(${element['id']});">ATTEND</button>
                                        </form>
                                        <form name="maybeform" method="POST">
                                            <input type="text" name="status" value="MAYBE" class="hide" required>
                                            <button type="button" class="delete maybe rsvp" onclick="maybeRsvp(${element['id']});">Maybe</button>
                                        </form>
                                        <form name="notatendform" method="POST">
                                            <input type="text" name="status" value="NOT ATTEND" class="hide" required>
                                            <button type="button" class="delete maybe rsvp" onclick="notAttendRsvp(${element['id']});">NOT ATTEND</button>
                                        </form>
                                    </div>
                                </div>
                        </div>
                    </div>
                </div>
                `
            user_meetupList.insertAdjacentHTML("afterbegin", all_meetup)
            let getbtn = document.querySelector(`.user${element['id']}`);
            let btn_hldr = document.querySelector(`.delete-holder${element['id']}`);
            if(element['rsvp']=='YES' || element['rsvp']=='MAYBE'){                
                btn_hldr.classList.toggle('hide');
                mtp_btn = `
                    <div class="btn-two"><button class="delete view-qns" onClick="getMeetupInfo(${element['id']});">Join Meetup</button></div>                    
                `
                getbtn.insertAdjacentHTML("beforeend",mtp_btn)
            }
            else if(element['rsvp']=='NOT ATTEND'){                
                btn_hldr.classList.toggle('hide');
                mtp_btn = `
                    <div class="btn-two"><button class="delete view-qns" style="background: black;">Not attending</button></div>                    
                `
                getbtn.insertAdjacentHTML("beforeend",mtp_btn)
            }
            else{
                mtp_btn = `
                    <div class="btn-two"><p>No reservations made</p></div>                    
                `
                getbtn.insertAdjacentHTML("beforeend",mtp_btn)
            }
        });
 
    }
    
})
.catch(error => console.log('bad request', error))

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
        window.location = "../../routes/user.html";
    }
        let user_person =`
                <p class="full-profile">${object['firstname']} ${object['lastname']}</p>         
            `
            let user_item = document.querySelector('.profile-name-holder')
            user_item.insertAdjacentHTML("afterbegin",user_person)
    
})
.catch(error => console.log('bad request', error))
function togglePass(){
        change_pass.classList.toggle('hide');
}
    chan_psw.addEventListener('click',()=>{
    change_pass.classList.toggle('hide');
})

function changePassword(){
    const url = 'https://questionerapplication.herokuapp.com/api/v2/user/auth/password';
    let form = document.forms['passwordform'];
    let formData = new FormData(form);
    let data = {};
    for (let [key, prop] of formData){
        data[key] = prop;
    }
    VALUE = JSON.stringify(data);
    fetch(url,{
        method: 'PATCH',
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
        string = object['message'];
        if(string == 'Token is invalid' || string == 'Permission denied!'){
            window.location = "../../routes/user.html";
        }            
            let psw_template=`
                <p class="err-msg">${string}</p>
            `
            let error_message= document.querySelector('.change-main-password')
            error_message.insertAdjacentHTML("beforeend", psw_template)
            
       
    })
    .catch(error => console.log('bad request', error))
}
function logOut(){
    localStorage.clear();
    window.location = "../../routes/user.html";
}