meetups = {}

class MeetupInfo:
    """ Meetup information from user input """
    def __init__(self, id, location, topic, happeningOn, tags, images=None):
        self.id = id
        self.location = location
        self.images = images
        self.topic = topic
        self.happeningOn = happeningOn
        self.tags = tags
        self.number_of_users = len(meetups) + 1   

    def add_meetup(self):
        """ takes the captured information and appends them to meetups db """
        db={
            "id":self.number_of_users,
            "location":self.location,
            "images":self.images,
            "topic":self.topic,
            "happeningOn":self.happeningOn,
            "tags":self.tags
        }
        #Append the db dictionary to meetups
        meetups.update({self.number_of_users:db})
        return meetups
    #static methods have no relationship with the class state
    @staticmethod
    def get_meetup(id):
        """ Check if meetup is present """
        for key_id, value in meetups.items():
            if key_id == id:
                return meetups[id]
        return {}

    @staticmethod
    def get_all_meetups():
        """ Gets all meetups """
        return(meetups)