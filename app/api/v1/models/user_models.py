users = {}

class UserInfo:
    """ Defines the user information """
    def __init__(self, id, firstname, lastname, othername, username, email, phoneNumber, password):
        self.id = id
        self.firstname = firstname
        self.lastname = lastname
        self.othername = othername
        self.username = username
        self.email = email
        self.phoneNumber = phoneNumber
        self.password = password
        self.number_of_users = len(users) + 1    

    def eachUser(self):
        """ Gets user information and appends to database """
        db={
            "id":self.number_of_users,
            "firstname":self.firstname,
            "lastname":self.lastname,
            "othername":self.othername,
            "username":self.username,
            "email":self.email,
            "phoneNumber":self.phoneNumber,
            "password":self.password
        }
        users.update({self.number_of_users:db})
        return users

    @staticmethod
    def get_user(id):
        """ returns specific user """
        return(users[id])

    @staticmethod
    def get_all_users():
        """ returns all users """
        return(users)