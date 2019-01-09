users = {}

meetup = {}

class UserInfo:
    def __init__(self, details, user_id):
        self.details = details
        self.user_id = user_id
        self.number_of_users = len(users) + 1    
    def eachUser(self):
        
        db = {"user_id":self.number_of_users}
        for k, v in self.details.items():
            if len(self.details) == 0:
                continue
            db.update({k:v})
            users.update({self.number_of_users:db})
        return users
    def specificUser(self):
        return(users[self.user_id])

class MeetupInfo:
    def __init__(self, meetups, meetup_id):
        self.meetups = meetups
        self.meetup_id = meetup_id
        self.number_of_users = len(users) + 1    
    def add_meetup(self):
        
        db = {"meetup_id":self.number_of_users}
        for k, v in self.meetups.items():
            if len(self.meetups) == 0:
                continue
            db.update({k:v})
            users.update({self.number_of_users:db})
        return users
    def specificUser(self):
        return(users[self.meetup_id])