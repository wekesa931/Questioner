let modalItem = document.querySelector('.success-modal');
let messageInfo = document.querySelector('.signupform-message');
let templateInfo = '';
function submitSignupInfo(){
    const url = 'http://127.0.0.1:5000/api/v2/user/auth/signup';
    let form = document.forms['signupForm'];
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
            'content-Type':'application/json'
        },
        body: VALUE
    })
    .then(response => response.json())
    .then(data => {
        console.log(data)
        let string = "";
        let object = data;

        for (let message in object) {
            string += object[message];
        }
        console.log(string)
        if(string == 'password must be at least 7 characters long, have at least one letter, one number and a special character'
            || string == 'email is not valid' || string == 'username is taken!' || string == 'Phone number already exists!'
            || string == 'email taken!'|| string == 'phoneNumber is missing a value' || string == 'email is missing a value' 
            || string == 'username is missing a value'|| string == 'othername is missing a value'|| string == 'lastname is missing a value'
            || string == 'firstname is missing a value' || string == 'password is missing a value'
                    ){
            templateInfo +=`
                <p>${string}</p>
            `
            messageInfo.innerHTML=""
            messageInfo.insertAdjacentHTML("beforeend", templateInfo)
        }
        else if(string == 'isRegistered'){
            modalItem.classList.toggle('hide');
            console.log('YES!')
        }
        
    })
    .catch(error => console.log('bad request', error))
}