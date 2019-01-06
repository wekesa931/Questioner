const sign_in = document.querySelector('.sign-in-module');
const sign_up = document.querySelector('.sign-up');
const sign_up_button = document.querySelector('.sign-up-module');
const sign_in_module = document.querySelector('.sign-in');


sign_in.addEventListener('click', ()=>{
    if(sign_up.classList.contains('hide')== false){
        sign_up.classList.toggle('hide');
        sign_in_module.classList.toggle('hide');
        sign_in.classList.toggle('sign-in-mode');
        sign_up_button.classList.toggle('sign-up-mode');
        sign_up_button.classList.toggle('sign-in-module');
    }
        
})

sign_up_button.addEventListener('click', ()=>{
    if(sign_up.classList.contains('hide')){
        sign_up.classList.toggle('hide');
        sign_in_module.classList.toggle('hide');
        sign_in.classList.toggle('sign-in-mode');
        sign_up_button.classList.toggle('sign-up-mode');
        sign_up_button.classList.toggle('sign-in-module');
    }
        
})