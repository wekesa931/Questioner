const navbar = document.querySelector('.fa-bars');
const formholder = document.querySelector('.add-meetup');
const psw = document.querySelector('.profile-info');
const pswchange = document.querySelector('.change-password');
const pswchangebtn = document.querySelector('.profile-name-holder');
const mainpswchange = document.querySelector('.change-full-profile');
const inpt = document.querySelector('.question-input');
const postqsn = document.querySelector('#btn-input');


navbar.addEventListener('click',()=>{
    formholder.classList.toggle('hide');
 })

 psw.addEventListener('click',()=>{
    pswchange.classList.toggle('hide');
})

pswchangebtn.addEventListener('click',()=>{
    mainpswchange.classList.toggle('hide');
})

postqsn.addEventListener('click',()=>{
    inpt.classList.toggle('hide');
})


