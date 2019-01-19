from urllib.parse import urlparse
import os
import psycopg2
from psycopg2.extras import RealDictCursor

class MeetupInfo:
    """ Defines the user information """
    def __init__(self, location, topic, happeningOn, tags, images):
        self.db_config = os.getenv('api_database_url')
        self.response = urlparse(self.db_config)
        self.config = {
            'database': self.response.path[1:],
            'user': self.response.username,
            'password': self.response.password,
            'host': self.response.hostname
        }
        self.location = location
        self.images = images
        self.topic = topic
        self.happeningOn = happeningOn
        self.tags = tags 

    def add_meetup(self):
        con, response = psycopg2.connect(**self.config), None
        cur = con.cursor(cursor_factory=RealDictCursor)
        try:
            query = "INSERT INTO meetups(location,images,topic,happeningOn,tags) VALUES(%s, %s, %s, %s, %s) RETURNING *; "
            cur.execute(query, (
                self.location, 
                self.images,
                self.topic,
                self.happeningOn,
                self.tags
            ))
            con.commit()
            response = cur.fetchone()
        except Exception as e:
            con.close()
        con.close()
        return response

    @staticmethod
    def get_meetups():
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
            query = "SELECT * FROM meetups; "
            cur.execute(query)
            meetups = cur.fetchall()
            con.close()
            return meetups
        except Exception as e:
            con.close()
            return e

    @staticmethod
    def del_meetup(meetup_id):
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
            query = "DELETE FROM meetups WHERE id='{}'".format(meetup_id)
            cur.execute(query)
            con.close()
            return True
        except Exception as e:
            con.close()
            return False