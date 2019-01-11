meetups = {}

class MeetupInfo:
    def __init__(self, id, createdOn, location, topics, happeningOn, tags, images=None):
        self.id = id
        self.createdOn = createdOn
        self.location = location
        self.images = images
        self.topics = topics
        self.happeningOn = happeningOn
        self.tags = tags
        self.number_of_users = len(meetups) + 1   

    def add_meetup(self):
        db={
            "id":self.number_of_users,
            "createdOn":self.createdOn,
            "location":self.location,
            "images":self.images,
            "topics":self.topics,
            "happeningOn":self.happeningOn,
            "tags":self.tags
        }
   
        meetups.update({self.number_of_users:db})
        return meetups
    @staticmethod
    def get_meetup(id):
        return(meetups[id])

    @staticmethod
    def get_all_meetups():
        return(meetups)

class Reservation:
    def __init__(self, id):
        self.id = id
        identified_meetup = meetups[self.id]
        self.db={
            "meetup":self.id,
            "topic":identified_meetup["topics"]
        }

    def attend_meetup(self):
        self.db["response"] = "YES"        
        return self.db
        
    def reject_meetup(self):
        self.db["response"] = "NO"        
        return self.db

    def not_certain(self):
        self.db["response"] = "MAYBE"        
        return self.db