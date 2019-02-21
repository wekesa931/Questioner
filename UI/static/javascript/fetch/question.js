let new_qsn_string = '';
let commErrorMessage='';
let new_comment_item = '';

function submitQuestionInfo(metup_id){
    const url = 'http://127.0.0.1:5000/api/v2/'+ metup_id +'/question';
    let form = document.forms['questionform'];
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
        let string = "";
        let object = data;
        for (let message in object) {
            string += object[message];
        }
        if(string == 'Token is invalid' || string == 'Permission denied!'){
            window.location = "file:///home/wekesa/Desktop/Questioner-gh-pages/UI/routes/user.html";
        }
        else if(string == 'body is missing a value' || string == 'title is missing a value' 
                            || string == 'A question with that title already exists in this meetup!'
                            || string == 'A similar question exists in this meetup!'){
            
            errorMessage +=`
                <p>${string}</p>
            `
            let question_template = document.querySelector('.modal-question-input');
            question_template.insertAdjacentHTML("beforeend", errorMessage)
            
        }
        else{
            let question_feedback = object['Questions']
            new_qsn_string = `
                    <div class="modal-user modal-question-item-holder">
                        <div class="modal-meetup-title-holder"><h3></h3></div>
                        <div class="modal-date-holder">Posted on ${question_feedback['createdon']} BY:&nbsp;&nbsp;<b>${question_feedback['firstname']} ${question_feedback['lastname']}</b></div>
                        <div class="modal-meetup-details">
                            <p>
                                ${question_feedback['title']}
                            </p>
                            <p>
                                ${question_feedback['body']}
                            </p>
                        </div>
                        <form name="commentform${question_feedback['id']}" method="POST">
                            <div class="modal-comment${question_feedback['id']}">
                                <textarea name="comment" value="Post Comment"></textarea>
                            </div>
                            <div class="modal-sub-btn">
                                    <input type="button" value="Post Comment" class="modal-post-question" onclick="submitCommentInfo(${question_feedback['id']});">
                            </div>
                        </form>

                        <div class="modal-vote modal-vote${question_feedback['id']}">
                            <i class="fa fa-thumbs-up" onclick="upvoteInfo(${question_feedback['id']})"></i>
                                <div class="votes-holder votes-holder${question_feedback['id']}">
                                    ${question_feedback['votes']}                        
                                </div>
                            <i class="fa fa-thumbs-down" onclick="downvoteInfo(${question_feedback['id']})"></i>
                        </div>

                        <div class="com-item modal-comment-statements${question_feedback['id']}"></div>

                    </div>
                `
                let new_question = document.querySelector('.append-items');
                new_question.insertAdjacentHTML("afterbegin", new_qsn_string);
        }
   })
    .catch(error => console.log('bad request', error))
}