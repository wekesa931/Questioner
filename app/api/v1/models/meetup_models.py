meetups = {}

class MeetupInfo:
    def __init__(self, id, location, topic, happeningOn, tags, images=None):
        self.id = id
        self.location = location
        self.images = images
        self.topic = topic
        self.happeningOn = happeningOn
        self.tags = tags
        self.number_of_users = len(meetups) + 1   

    def add_meetup(self):
        db={
            "id":self.number_of_users,
            "location":self.location,
            "images":self.images,
            "topic":self.topic,
            "happeningOn":self.happeningOn,
            "tags":self.tags
        }
   
        meetups.update({self.number_of_users:db})
        return meetups
    @staticmethod
    def get_meetup(id):
        for key_id, value in meetups.items():
            if key_id == id:
                return meetups[id]
        return {}

    @staticmethod
    def get_all_meetups():
        return(meetups)