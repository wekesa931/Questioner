function upvoteInfo(question_id){
    const url = 'https://questionerapplication.herokuapp.com/api/v2/' + question_id + '/upvote';
    fetch(url,{
        method: 'PATCH',
        headers: {
            'Authorization': `Bearer ${localStorage['currentuser']}`,
            'content-Type':'application/json'
        }
    })
    .then(response => response.json())
    .then(data => {
        let string = "";
        let object = data;
        if(object['message']=='You have already voted'){
            let vote_modal = document.querySelector(`.modal-vote${question_id}`);
            let message_item=`
                <p>${object['message']}</p>
            `
            vote_modal.insertAdjacentHTML("afterbegin",message_item)
        }
        else{
            let votes_container = document.querySelector(`.votes-holder${question_id}`);
            votes_container.innerHTML= object['votes'];
        }
   })
    .catch(error => console.log('bad request', error))
}

function downvoteInfo(question_id){
    const url = 'https://questionerapplication.herokuapp.com/api/v2/' + question_id + '/downvote';
    fetch(url,{
        method: 'PATCH',
        headers: {
            'Authorization': `Bearer ${localStorage['currentuser']}`,
            'content-Type':'application/json'
        }
    })
    .then(response => response.json())
    .then(data => {
        let string = "";
        let object = data;
        if(object['message']=='You have already voted'){
            let vote_modal = document.querySelector(`.modal-vote${question_id}`);
            let message_item=`
                <p>${object['message']}</p>
            `
            vote_modal.insertAdjacentHTML("afterbegin",message_item)
        }
        else{
            let votes_container = document.querySelector(`.votes-holder${question_id}`);
            votes_container.innerHTML= object['votes'];
        }
   })
    .catch(error => console.log('bad request', error))
}