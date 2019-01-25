import psycopg2
from psycopg2.extras import RealDictCursor
from app.api.v2.database.db_configs import database_configuration

class AddImage:
    """ Defines the details of te user """
    def __init__(self,meetup_id,topic,image):
        self.config = database_configuration()
        self.meetup_id = meetup_id
        self.topic = topic
        self.image = image

    def add_image(self):
        """ Appends user information to user db """
        con = psycopg2.connect(**self.config)
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
        except Exception:
            con.close()
        con.close()
        return response

    @staticmethod
    def get_image():
        config = database_configuration()
        con = psycopg2.connect(**config)
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
