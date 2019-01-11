questions = {}

class AddQuestion:
    def __init__(self, id, createdOn, meetup_id, title, body):
        self.id = id
        self.createdOn = createdOn
        self.meetup_id = meetup_id
        self.title = title
        self.body = body
        self.number_of_questions = len(questions) + 1   
        self.votes = 0
    def add_question(self):
        db={
            "id":self.number_of_questions,
            "createdOn":self.createdOn,
            "meetup":self.meetup_id,
            "title":self.title,
            "body":self.body,
            "votes":self.votes
        }
   
        questions.update({self.number_of_questions:db})
        return questions
    @staticmethod
    def get_question(id):
        return(questions[id])

    @staticmethod
    def update_question_upvote(id):
        questions[id]['votes'] += 1

    @staticmethod
    def update_question_downvote(id):
        questions[id]['votes'] -= 1