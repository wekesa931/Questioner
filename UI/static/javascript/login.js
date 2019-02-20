function submitInfo(){
    const url = 'http://127.0.0.1:5000/api/v2/user/auth/login';
    let form = document.forms['loginForm'];
    let formData = new FormData(form);
    let data = {};
    for (let [key, prop] of formData){
        data[key] = prop;
    }
    VALUE = JSON.stringify(data, null, 2);
    fetch(url,{
        method: 'POST',
        headers: {
            'content-Type':'application/json'
        },
        body: VALUE
    })
    .then(response => response.json())
    .then(data => {
        let object = data;
        localStorage.setItem('currentuser',object['token']);
        for (let message in object) {
            let message_item =object[message];
            if(object[message] == 'Username not found!' || object[message] == 'Wrong password!' ){
                let string =`
                <p>${message_item}</p>
            `
            let message = document.querySelector('.form-message');
            message.insertAdjacentHTML("beforeend", string)
            }
            else if(object['isadmin'] == true){
                window.location = "file:///home/wekesa/Desktop/Questioner-gh-pages/UI/routes/admin.html";
            }
            else if(object['isadmin'] == false){
                window.location = "file:///home/wekesa/Desktop/Questioner-gh-pages/UI/routes/dashboard.html";
            }
        }
    })
    .catch(error => console.log('bad request', error))
}
