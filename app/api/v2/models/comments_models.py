from urllib.parse import urlparse
import os
import psycopg2
from psycopg2.extras import RealDictCursor

class AddComment:
    """ Defines the details of te user """
    def __init__(self, user_id, question_id, comment):
        self.db_config = os.getenv('api_database_url')
        self.response = urlparse(self.db_config)
        self.config = {
            'database': self.response.path[1:],
            'user': self.response.username,
            'password': self.response.password,
            'host': self.response.hostname
        }
        self.user_id = user_id
        self.question_id = question_id
        self.comment = comment

    def add_comment(self):
        """ Appends user information to user db """
        con, response = psycopg2.connect(**self.config), None
        cur = con.cursor(cursor_factory=RealDictCursor)
        try:
            query = "INSERT INTO comments(user_id,question_id,comments) VALUES(%s,%s,%s) RETURNING *; "
            cur.execute(query, (
                self.user_id,
                self.question_id,
                self.comment
            ))
            con.commit()
            response = cur.fetchone()
        except Exception as e:
            con.close()
        con.close()
        return response

    @staticmethod
    def get_comments():
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
            query = "SELECT * FROM comments; "
            cur.execute(query)
            comments = cur.fetchall()
            con.close()
            return comments
        except Exception as e:
            con.close()
            return e