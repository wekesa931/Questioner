from urllib.parse import urlparse
import os
import psycopg2
from psycopg2.extras import RealDictCursor
from werkzeug.security import generate_password_hash

class UserInfo:
    """ Defines the user information """
    def __init__(self, firstname, lastname, othername, username, email, phoneNumber, password, isAdmin):
        self.db_config = os.getenv('api_database_url')
        self.response = urlparse(self.db_config)
        self.config = {
            'database': self.response.path[1:],
            'user': self.response.username,
            'password': self.response.password,
            'host': self.response.hostname
        }
        self.firstname = firstname
        self.lastname = lastname
        self.othername = othername
        self.username = username
        self.email = email
        self.phoneNumber = phoneNumber
        self.password = generate_password_hash(password)
        self.isAdmin = isAdmin  

    def add_user(self):
        con, response = psycopg2.connect(**self.config), None
        cur = con.cursor(cursor_factory=RealDictCursor)
        try:
            query = "INSERT INTO users(firstname,lastname,othername,username,email,phoneNumber,password,isAdmin) VALUES(%s,%s,%s,%s,%s,%s,%s,%s) RETURNING *; "
            cur.execute(query, (
                self.firstname, 
                self.lastname,
                self.othername,
                self.username,
                self.email,
                self.phoneNumber,
                self.password,
                self.isAdmin
            ))
            con.commit()
            response = cur.fetchone()
        except Exception as e:
            con.close()
        con.close()
        return response

    @staticmethod
    def get_all_users():
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
            query = "SELECT * FROM users;"
            cur.execute(query)
            users = cur.fetchall()
            con.close()
            return users
        except Exception as e:
            con.close()
            return e
    
    @staticmethod
    def get_one_user(user_id):
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
            query = "SELECT * FROM users WHERE id='{}'".format(user_id)
            cur.execute(query)
            users = cur.fetchone()
            con.close()
            return users
        except Exception as e:
            con.close()
            return e

    @staticmethod
    def get_admin(user_id):
        user = UserInfo.get_one_user(user_id)
        if user['isadmin'] == True:
            return True
        return False
    