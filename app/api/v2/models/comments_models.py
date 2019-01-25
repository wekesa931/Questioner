import psycopg2
from psycopg2.extras import RealDictCursor
from app.api.v2.database.db_configs import database_configuration

class AddComment:
    """ Defines the details of te user """
    def __init__(self, user_id, question_id, comment):
        self.config = database_configuration()
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
        except Exception:
            con.close()
        con.close()
        return response

    @staticmethod
    def get_comments():
        config = database_configuration()
        con = psycopg2.connect(**config)
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