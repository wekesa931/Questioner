from urllib.parse import urlparse
import os
import psycopg2
from psycopg2.extras import RealDictCursor

class AddImage:
    """ Defines the details of te user """
    def __init__(self,meetup_id,topic,image):
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
        self.image = image

    def add_image(self):
        """ Appends user information to user db """
        con, response = psycopg2.connect(**self.config), None
        cur = con.cursor(cursor_factory=RealDictCursor)
        try:
            query = "INSERT INTO images(meetup_id,topic,image) VALUES(%s,%s,%s) RETURNING *; "
            cur.execute(query, (
                self.meetup_id, 
                self.topic,
                self.image
            ))
            con.commit()
            response = cur.fetchone()
        except Exception as e:
            con.close()
        con.close()
        return response

    @staticmethod
    def get_image():
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
            query = "SELECT * FROM images; "
            cur.execute(query)
            image = cur.fetchall()
            con.close()
            return image
        except Exception as e:
            con.close()
            return e

    @staticmethod
    def single_image(meetup_id):
        image_list = []
        all_images=AddImage.get_image()
        for image in all_images:
            if image['meetup_id'] == meetup_id:
                image_item = image['image']
                image_list.append(image_item)
        return image_list
