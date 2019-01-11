meetups = {}

class MeetupInfo:
    def __init__(self, id, location, topics, happeningOn, tags, images=None):
        self.id = id
        self.location = location
        self.images = images
        self.topics = topics
        self.happeningOn = happeningOn
        self.tags = tags
        self.number_of_users = len(meetups) + 1   

    def add_meetup(self):
        db={
            "id":self.number_of_users,
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
    def __init__(self, meetup_id, topic, status):
        self.meetup_id = meetup_id
        self.topic = topic
        self.status = status
        self.db={
            "meetup":self.meetup_id,
            "topic":self.topic
        }

    def meetup_status(self):
        self.db["status"] = self.status        
        return self.db
