from urllib.parse import urlparse
import os
import psycopg2
from psycopg2.extras import RealDictCursor

class AddTags:
    """ Defines the details of te user """
    def __init__(self,meetup_id,topic,tag_item):
        self.db_config = os.getenv('api_database_url')
        self.response = urlparse(self.db_config)
        self.config = {
            'database': self.response.path[1:],
            'user': self.response.username,
            'password': self.response.password,
            'host': self.response.hostname
        }
        self.meetup_id = meetup_id
        self.topic = topic
        self.tag_item = tag_item

    def add_tags(self):
        """ Appends user information to user db """
        con, response = psycopg2.connect(**self.config), None
        cur = con.cursor(cursor_factory=RealDictCursor)
        try:
            query = "INSERT INTO tags(meetup_id,topic,tag_item) VALUES(%s,%s,%s) RETURNING *; "
            cur.execute(query, (
                self.meetup_id, 
                self.topic,
                self.tag_item
            ))
            con.commit()
            response = cur.fetchone()
        except Exception as e:
            con.close()
        con.close()
        return response

    @staticmethod
    def get_tags():
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
            query = "SELECT * FROM tags; "
            cur.execute(query)
            tags = cur.fetchall()
            con.close()
            return tags
        except Exception as e:
            con.close()
            return e