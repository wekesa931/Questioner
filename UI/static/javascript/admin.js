const navbar = document.querySelector('.fa-bars');
const formholder = document.querySelector('.add-meetup');
const psw = document.querySelector('.profile-info');
const pswchange = document.querySelector('.change-password');
const pswchangebtn = document.querySelector('.profile-name-holder');
const mainpswchange = document.querySelector('.change-full-profile');
const inpt = document.querySelector('.question-input');
const postqsn = document.querySelector('#btn-input');
const viewqsn = document.querySelector('.view-qs');
const qsn_views = document.querySelector('.view-meetup');
const viewcmn = document.querySelector('.view-comments');
const cmnbtn = document.querySelector('.comments');


navbar.addEventListener('click',()=>{
    formholder.classList.toggle('hide');
 })

pswchangebtn.addEventListener('click',()=>{
    mainpswchange.classList.toggle('hide');
})

 cmnbtn.addEventListener('click',()=>{
    viewcmn.classList.toggle('hide-item-view');
 })
 viewqsn.addEventListener('click',()=>{
    qsn_views.classList.toggle('hide-item-view');
 })

 postqsn.addEventListener('click',()=>{
    inpt.classList.toggle('hide');
})
