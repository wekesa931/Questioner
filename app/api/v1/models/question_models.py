""" User models """
import datetime #used to set the date

questions = {}
today = datetime.date.today()

class AddQuestion:
    """ Defines the details of te user """
    def __init__(self, id, meetup_id, title, body):
        self.id = id
        self.meetup_id = meetup_id
        self.title = title
        self.body = body
        self.number_of_questions = len(questions) + 1   
        self.votes = 0
    def add_question(self):
        """ Appends user information to user db """
        db={
            "id":self.number_of_questions,
            "createdOn":"{:%d, %b %Y}".format(today),
            "meetup":self.meetup_id,
            "title":self.title,
            "body":self.body,
            "votes":self.votes,
            "isAdmin":"False"
        }
        questions.update({self.number_of_questions:db})
        return questions
    @staticmethod
    def get_question(id):
        """ static method to get a specific question """
        for key_id, value in questions.items():
            if key_id == id:
                return questions[id]
        return {}

    @staticmethod
    def update_question_upvote(id):
        """ Updates the votes for a question when upvoted """
        questions[id]['votes'] += 1

    @staticmethod
    def update_question_downvote(id):
        """ Updates the votes for a question when downvoted """
        questions[id]['votes'] -= 1