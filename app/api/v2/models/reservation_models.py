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
        con = psycopg2.connect(**self.config)
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
        except Exception:
            con.close()
        con.close()
        return response

    @staticmethod
    def get_reservations():
        config = database_configuration()
        con= psycopg2.connect(**config)
        cur = con.cursor(cursor_factory=RealDictCursor)
        try:
            query = "SELECT * FROM reservations; "
            cur.execute(query)
            reservations = cur.fetchall()
            con.close()
            return reservations
        except Exception as e:
            con.close()
            return e

    @staticmethod
    def attendance():
        all_reservations = Reservation.get_reservations()
        my_reservations = []
        for reservation in all_reservations:
            if reservation['status'] == "YES" or reservation['status'] == "MAYBE":
                my_reservations.append(reservation)
        return my_reservations