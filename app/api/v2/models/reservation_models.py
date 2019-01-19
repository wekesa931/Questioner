from urllib.parse import urlparse
import os
import psycopg2
from psycopg2.extras import RealDictCursor

class Reservation:
    """ Defines reservations status """
    def __init__(self, user_id, meetup_id, topic, status):
        self.db_config = os.getenv('api_database_url')
        self.response = urlparse(self.db_config)
        self.config = {
            'database': self.response.path[1:],
            'user': self.response.username,
            'password': self.response.password,
            'host': self.response.hostname
        }
        self.user_id = user_id
        self.meetup_id = meetup_id
        self.topic = topic
        self.status = status

    def make_reservation(self):
        con, response = psycopg2.connect(**self.config), None
        cur = con.cursor(cursor_factory=RealDictCursor)
        try:
            query = "INSERT INTO reservations(user_id,meetup_id,topic,status) VALUES(%s, %s, %s, %s) RETURNING *; "
            cur.execute(query, (
                self.user_id, 
                self.meetup_id,
                self.topic,
                self.status
            ))
            con.commit()
            response = cur.fetchone()
        except Exception as e:
            con.close()
        con.close()
        return response