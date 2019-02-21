function attendRsvp(metup_id){
    const url = 'http://127.0.0.1:5000/api/v2/'+ metup_id +'/rsvp';
    let btn_hldr = document.querySelector(`#btn-holer${metup_id}`);
    btn_hldr.classList.toggle('hide');
    let form = document.forms['attendform'];
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
        location.reload();
        let string = "";
        let object = data;
        console.log(object);
   })
    .catch(error => console.log('bad request', error))
}

function maybeRsvp(metup_id){
    const url = 'http://127.0.0.1:5000/api/v2/'+ metup_id +'/rsvp';
    let form = document.forms['maybeform'];
    let formData = new FormData(form);
    let data = {};
    for (let [key, prop] of formData){
        data[key] = prop;
    }
    VALUE = JSON.stringify(data);
    console.log(VALUE);
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
        location.reload();
        let string = "";
        let object = data;
        console.log(object);
   })
    .catch(error => console.log('bad request', error))
}

function notAttendRsvp(metup_id){
    const url = 'http://127.0.0.1:5000/api/v2/'+ metup_id +'/rsvp';
    fetch(url,{
        method: 'POST',
        headers: {
            'Authorization': `Bearer ${localStorage['currentuser']}`,
            'content-Type':'application/json'
        },
        body: {
            'status': 'NOT ATTEND'
        }
    })
    .then(response => response.json())
    .then(data => {
        location.reload();
        let string = "";
        let object = data;
        console.log(object);
   })
    .catch(error => console.log('bad request', error))
}