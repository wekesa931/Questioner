let qsn_template = document.querySelector('.qsn-template');
let qsn_count = document.querySelector('#counter');
let qsn_feeds = document.querySelector('.qsn_feeds');


qsn_url = 'https://questionerapplication.herokuapp.com/api/v2/user/questions';
fetch(qsn_url,{
method: 'GET',
headers: {
    'Authorization': `Bearer ${localStorage['currentuser']}`,
    'content-Type':'application/json'
},
})
.then(response => response.json())
.then(data =>
{



let class_id = 0;
let qsn_string = "";
let string = "";
let object = data;
let question_couter = 0;
for(let item in object){
    qsn_string += object[item];   
    if(qsn_string == 'Token is invalid' || qsn_string == 'Token is missing!'){
        window.location = "../../routes/user.html";
    }
    else if(qsn_string == 'you have not posted any question'){
        string = `
            <div id="qsn_item">
                <p>You have not posted any question</p>
            </div>
        `
        qsn_template.insertAdjacentHTML("afterbegin", string);
    }
    else{


    let bodyItem = object[item];

    bodyItem.forEach(element => {
        question_couter +=1;
        class_id +=1;
        let qsn_item = element['Question'];        
        string = `
            <div id="qsn_item">
                <div class="meetup-title-holder"><p>${element['meetup topic']}</p></div>
                
                <div class="meetup-details meetup-border">
                    <p>
                        ${qsn_item['body']}
                    </p>
                    <div class="delete-holder ">
                        <div class="btn-one-view"><button class="delete comments${class_id}">View comments</button></div>                      
                    </div>
                    <div class="view-comments hide">
                    </div>
                </div> 
            </div>
    
        `
        
        qsn_template.insertAdjacentHTML("afterbegin", string);
        let view_comment_button = document.querySelector(`.comments${class_id}`);
        let viewComments = document.querySelector('.view-comments');
        view_comment_button.addEventListener('click', ()=>{
        viewComments.classList.toggle('hide');
    })

        element['comments'].forEach(com_item =>{
            let comm_string = `
                <p>
                    ${com_item['comments']}
                    <span><h4>- ${com_item['firstname']} ${com_item['lastname']}</h4></span>
                </p>
                `
            let comment_template = document.querySelector('.view-comments');
            comment_template.insertAdjacentHTML("afterbegin", comm_string);
            })
        });

    }
}
    qsn_count.innerHTML=question_couter;
    
})
.catch(error => console.log('bad request', error))




function questionFeeds(){

    qsnFeds_url = 'https://questionerapplication.herokuapp.com/api/v2/users/questions';
    fetch(qsnFeds_url,{
    method: 'GET',
    headers: {
        'Authorization': `Bearer ${localStorage['currentuser']}`,
        'content-Type':'application/json'
    },
    })
    .then(response => response.json())
    .then(data =>
    {
    let qsn_string="";    
    let feedString = '';
    let object_feed = data;
    for(let item_feed in object_feed){
        qsn_string += object_feed[item_feed];   
        if(qsn_string == 'Token is invalid' || qsn_string == 'Token is missing!'){
            window.location = "../../routes/user.html";
        }
        else if(qsn_string == 'no questions found'){
            feedString = `
                <div id="qsn_item">
                    <p>No Questions feeds available</p>
                </div>
            `
            qsn_feeds.insertAdjacentHTML("afterbegin", feedString);
        }
    else{
        let feed_item = object_feed[item_feed];
        feed_item.forEach(element =>{
        feedString = `
            <div id="qsn_item">
                <div class="meetup-title-holder"><p>${element['topic']}</p></div>
                    <div class="meetup-details meetup-border">
                        <p>
                            ${element['body']}
                            <span><h4>- ${element['firstname']} ${element['lastname']}</h4></span>
                        </p>
                </div> 
            </div>
            `
            qsn_feeds.insertAdjacentHTML("afterbegin", feedString);
        })  
    }               
}})

.catch(error => console.log('bad request', error))
}
questionFeeds();