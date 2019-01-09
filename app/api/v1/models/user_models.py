users = {}

meetups = {}

questions = {}

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

class FetchMeetup:
    def __init__(self, meetup_id):
        self.meetup_id = meetup_id  
        
    def get_meetup(self):
        return(meetups[self.meetup_id])


class AddQuestion:
    def __init__(self, id, createdOn, meetup, title, body, votes):
        self.id = id
        self.createdOn = createdOn
        self.meetup = meetup
        self.title = title
        self.body = body
        self.votes = votes
        self.number_of_questions = len(questions) + 1   

    def add_question(self):
        db={
            "id":self.number_of_questions,
            "createdOn":self.createdOn,
            "meetup":self.meetup,
            "title":self.title,
            "body":self.body,
            "votes":self.votes
        }
   
        questions.update({self.number_of_questions:db})
        return questions
    def specificQuestion(self):
        return(questions[self.id])