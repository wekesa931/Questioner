users = {}

class UserInfo:
    def __init__(self, details, user_id):
        self.details = details
        self.user_id = user_id
        self.number_of_users = len(users) + 1    
    def eachUser(self):
        
        db = {"id":self.number_of_users}
        for k, v in self.details.items():
            if len(self.details) == 0:
                continue
            db.update({k:v})
            users.update({self.number_of_users:db})
        return users
    def specificUser(self):
        return(users[self.user_id])