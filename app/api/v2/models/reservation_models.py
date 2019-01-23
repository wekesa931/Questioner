import psycopg2
from psycopg2.extras import RealDictCursor
from app.api.v2.database.db_configs import database_configuration

class Reservation:
    """ Defines reservations status """
    def __init__(self, user_id, meetup_id, topic, status):
        self.config = database_configuration()
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