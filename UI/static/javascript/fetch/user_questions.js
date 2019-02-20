function questionFeeds(){

    qsnFeds_url = 'http://127.0.0.1:5000/api/v2/users/questions';
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
    let feedString = '';
    let object_feed = data;
    for(let item_feed in object_feed){
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
}})

.catch(error => console.log('bad request', error))
}
questionFeeds();