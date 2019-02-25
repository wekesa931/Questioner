fetch('https://questionerapplication.herokuapp.com/api/v2/user/auth/users',{
    method: 'GET',
    headers: {
        'Authorization': `Bearer ${localStorage['currentuser']}`,
        'content-Type':'application/json'
    },
})
.then(response => response.json())
.then(data => {
    let user_string = "";
    let object = data;
    for (let message in object) {
        object[message].forEach(element => {
            user_string =`
                <div class="modal-user">
                    <div class="user-name">
                        <p>First name: <b>${element['firstname']}</b></p>
                        <p>last name: <b>${element['lastname']}</b></p>
                        <p>Middle name: <b>${element['othername']}</b></p>
                        <p>Username: <b>${element['username']}</b></p>
                        <p>Email: <b>${element['email']}</b></p>
                        <p>Phone number: <b>${element['phonenumber']}</b></p>
                    </div>
                    <div class="user-info">
                            

                    </div>
                </div>
            `
            let append_user_items=document.querySelector('.append-user-items')
            append_user_items.insertAdjacentHTML("afterbegin",user_string)

            if(element['isadmin'] == false){
                let string_item=`
                    <p>User type: <b>Normal User</b></p>
                    <div class="make-admin">
                        <button onclick="makeAdmin(${element['id']});">Make Admin</button>
                    </div>`
                let user_info = document.querySelector('.user-info')
                user_info.insertAdjacentHTML("beforeend",string_item)
            } else{
                let string_item=`
                    <p>User type: <b>Admin User</b></p>
                    <div class="make-admin">
                        <button onclick="removeAdmin(${element['id']});">Remove Admin</button>
                    </div>
                    `
                let user_info = document.querySelector('.user-info')
                user_info.insertAdjacentHTML("beforeend",string_item)
            }

        })
    }
    
})
.catch(error => console.log('bad request', error))

function makeAdmin(user_id){
    fetch('https://questionerapplication.herokuapp.com/api/v2/user/auth/'+user_id+'/admin',{
    method: 'PATCH',
    headers: {
        'Authorization': `Bearer ${localStorage['currentuser']}`,
        'content-Type':'application/json'
    },
    })
    .then(response => response.json())
    .then(data => {console.log(data)
    })
    .catch(error => console.log('bad request', error))
    location.reload()
}
function removeAdmin(user_id){
    fetch('https://questionerapplication.herokuapp.com/api/v2/user/auth/'+user_id+'/_admin',{
    method: 'PATCH',
    headers: {
        'Authorization': `Bearer ${localStorage['currentuser']}`,
        'content-Type':'application/json'
    },
    })
    .then(response => response.json())
    .then(data => {console.log(data)
    })
    .catch(error => console.log('bad request', error))
    location.reload()
}