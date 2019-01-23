import psycopg2
from psycopg2.extras import RealDictCursor
from app.api.v2.database.db_configs import database_configuration

class AddTags:
    """ Defines the details of te user """
    def __init__(self,meetup_id,topic,tag_item):
        self.config = database_configuration()
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
        config = database_configuration()
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

    @staticmethod
    def single_tag(meetup_id):
        tag_list = []
        all_tags=AddTags.get_tags()
        for tag in all_tags:
            if tag['meetup_id'] == meetup_id:
                tag_item = tag['tag_item']
                tag_list.append(tag_item)
        return tag_list