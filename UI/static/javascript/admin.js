let user_btn = document.querySelector('#all-users');
let user_modal = document.querySelector('.user-modal');

user_btn.addEventListener('click', ()=>{
   user_modal.classList.toggle('modal-hide');
})
/* const navbar = document.querySelector('.fa-bars');
const formholder = document.querySelector('.add-meetup');
const psw = document.querySelector('.profile-info');
const pswchange = document.querySelector('.change-password');
const pswchangebtn = document.querySelector('.profile-name-holder');
const mainpswchange = document.querySelector('.change-full-profile');
const viewqsn = document.querySelector('.view-qs');
const qsn_views = document.querySelector('.view-meetup');
const viewcmn = document.querySelector('.view-comments');
const cmnbtn = document.querySelector('.comments'); */

//const close_window = document.querySelector('.fa-window-close');
//const mtp_item = document.querySelector('.meetup-modal');
//const inpt = document.querySelector('.modal-question-input');
//const postqsn = document.querySelector('.modal-question-input');
   let textarea = document.querySelector('.topictext');
   textarea.addEventListener('keydown', autosize);             
   function autosize(){
      var el = this;
      setTimeout(function(){
         el.style.cssText = 'height:auto; padding:0';
         el.style.cssText = 'height:' + el.scrollHeight + 'px';
      },0);
   }


/* function postQuestion(){
   inpt.classList.toggle('modal-hide');
} */

/* navbar.addEventListener('click',()=>{
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
 }) */
/* close_window.addEventListener('click', ()=>{
   mtp_item.classList.toggle('modal-hide');
})  */  
/* postqsn.addEventListener('click',()=>{
    console.log('yeees');
    inpt.classList.toggle('modal-hide');
}) */
