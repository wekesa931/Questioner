import psycopg2
from psycopg2.extras import RealDictCursor
from app.api.v2.database.db_configs import database_configuration

class MeetupInfo:
    """ Defines the user information """
    def __init__(self, user_id, location, topic, happeningOn, tags, images):
        self.config = database_configuration()
        self.user_id = user_id
        self.location = location
        self.images = images
        self.topic = topic
        self.happeningOn = happeningOn
        self.tags = tags 

    def add_meetup(self):
        con, response = psycopg2.connect(**self.config), None
        cur = con.cursor(cursor_factory=RealDictCursor)
        try:
            query = "INSERT INTO meetups(user_id,location,images,topic,happeningOn,tags) VALUES(%s, %s, %s, %s, %s, %s) RETURNING *; "
            cur.execute(query, (
                self.user_id,
                self.location, 
                self.images,
                self.topic,
                self.happeningOn,
                self.tags
            ))
            con.commit()
            response = cur.fetchone()
        except Exception:
            con.close()
        con.close()
        return response

    @staticmethod
    def get_meetups():
        config = database_configuration()
        con= psycopg2.connect(**config)
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
    def get_one_meetup(meetup_id):
        config = database_configuration()
        con = psycopg2.connect(**config)
        cur = con.cursor(cursor_factory=RealDictCursor)
        try:
            query = "SELECT * FROM meetups WHERE id='{}'".format(meetup_id)
            cur.execute(query)
            meetup = cur.fetchone()
            con.close()
            return meetup
        except Exception as e:
            con.close()
            return e

    @staticmethod
    def del_meetup(meetup_id):
        config = database_configuration()
        con = psycopg2.connect(**config)
        cur = con.cursor(cursor_factory=RealDictCursor)
        try:
            query = "DELETE FROM meetups WHERE id='{}';".format(meetup_id)
            cur.execute(query)
            con.commit()
            con.close()
            return True
        except Exception as e:
            con.close()
            return e