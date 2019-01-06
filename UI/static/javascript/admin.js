const navbar = document.querySelector('.fa-bars');
const formholder = document.querySelector('.add-meetup');
const btn = document.querySelector('.create-meetup-button');



navbar.addEventListener('click',()=>{
    formholder.classList.toggle('hide');
 })

btn.addEventListener('click',()=>{
    formholder.classList.toggle('hide');
})