from urllib.parse import urlparse
import os
import psycopg2
from psycopg2.extras import RealDictCursor

class AddQuestion:
    """ Defines the details of te user """
    def __init__(self, user_id, meetup_id, title, body):
        self.db_config = os.getenv('api_database_url')
        self.response = urlparse(self.db_config)
        self.config = {
            'database': self.response.path[1:],
            'user': self.response.username,
            'password': self.response.password,
            'host': self.response.hostname
        }
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
        except Exception as e:
            con.close()
        con.close()
        return response

    @staticmethod
    def get_questions():
        db_config = os.getenv('api_database_url')
        response = urlparse(db_config)
        config = {
            'database': response.path[1:],
            'user': response.username,
            'password': response.password,
            'host': response.hostname
        }
        con, response = psycopg2.connect(**config), None
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
        db_config = os.getenv('api_database_url')
        response = urlparse(db_config)
        config = {
            'database': response.path[1:],
            'user': response.username,
            'password': response.password,
            'host': response.hostname
        }
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
        except Exception as e:
            con.close()
            response = False
        con.close()
        return response
