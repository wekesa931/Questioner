users = {}

class UserInfo:
    def __init__(self, id, firstname, lastname, othername, email, phoneNumber, password):
        self.id = id
        self.firstname = firstname
        self.lastname = lastname
        self.othername = othername
        self.email = email
        self.phoneNumber = phoneNumber
        self.password = password
        self.number_of_users = len(users) + 1    

    def eachUser(self):
        db={
            "id":self.number_of_users,
            "firstname":self.firstname,
            "lastname":self.lastname,
            "othername":self.othername,
            "email":self.email,
            "phoneNumber":self.phoneNumber,
            "password":self.password
        }
        users.update({self.number_of_users:db})
        return users

    @staticmethod
    def get_user(id):
        return(users[id])

    @staticmethod
    def get_all_users():
        return(users)



