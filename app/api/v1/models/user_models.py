users = {}

class UserInfo:
    def __init__(self, details):
        self.details = details
        
    def eachUser(self):
        number_of_users = len(users) + 1
        db = {"id":number_of_users}
        for k, v in self.details.items():
            if len(self.details) == 0:
                continue
            db.update({k:v})
            users.update({number_of_users:db})
        return users