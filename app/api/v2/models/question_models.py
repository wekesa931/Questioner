import psycopg2
from psycopg2.extras import RealDictCursor
from app.api.v2.database.db_configs import database_configuration

class AddQuestion:
    """ Defines the details of te user """
    def __init__(self, user_id, meetup_id, title, body):
        self.config = database_configuration()
        self.createdBy = user_id
        self.meetup_id = meetup_id
        self.title = title
        self.body = body  
        self.votes = 0

    def add_question(self):
        """ Appends user information to user db """
        con, response = psycopg2.connect(**self.config), None
        cur = con.cursor(cursor_factory=RealDictCursor)
        try:
            query = "INSERT INTO question(createdBy,meetup_id,title,body,votes) VALUES(%s,%s,%s,%s,%s) RETURNING *; "
            cur.execute(query, (
                self.createdBy, 
                self.meetup_id,
                self.title,
                self.body,
                self.votes
            ))
            con.commit()
            response = cur.fetchone()
        except Exception:
            con.close()
        con.close()
        return response

    @staticmethod
    def get_questions():
        config = database_configuration()
        con = psycopg2.connect(**config)
        cur = con.cursor(cursor_factory=RealDictCursor)
        try:
            query = "SELECT * FROM question; "
            cur.execute(query)
            questions = cur.fetchall()
            con.close()
            return questions
        except Exception as e:
            con.close()
            return e

    @staticmethod
    def update_question(votes,question_id):
        config = database_configuration()
        con, response = psycopg2.connect(**config), None
        cur = con.cursor(cursor_factory=RealDictCursor)
        try:
            query = "UPDATE question SET votes=%s WHERE id=%s;"
            cur.execute(query, (
                votes, 
                question_id
            ))
            con.commit()
            response = True
        except Exception:
            con.close()
            response = False
        con.close()
        return response

    @staticmethod
    def get_one_question(question_id):
        all_questions = AddQuestion.get_questions()
        for question in all_questions:
            if question['id'] == question_id:
                return question
        return False
