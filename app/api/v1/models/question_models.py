questions = {}

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