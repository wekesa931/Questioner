function attendRsvp(metup_id){
    const url = 'https://questionerapplication.herokuapp.com/api/v2/'+ metup_id +'/rsvp';
    let form = document.forms['atendform'];
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
        let object = data;
        console.log(object);
   })
    .catch(error => console.log('bad request', error))
}

function maybeRsvp(metup_id){
    const url = 'https://questionerapplication.herokuapp.com/api/v2/'+ metup_id +'/rsvp';
    let form = document.forms['maybeform'];
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
        let object = data;
        console.log(object);
   })
    .catch(error => console.log('bad request', error))
}

function notAttendRsvp(metup_id){
    const url = 'https://questionerapplication.herokuapp.com/api/v2/'+ metup_id +'/rsvp';
    let form = document.forms['notatendform'];
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
        let object = data;
        console.log(object);
   })
    .catch(error => console.log('bad request', error))
}