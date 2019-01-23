import psycopg2
from psycopg2.extras import RealDictCursor
from werkzeug.security import generate_password_hash
from app.api.v2.database.db_configs import database_configuration

class UserInfo:
    """ Defines the user information """
    def __init__(self, firstname, lastname, othername, username, email, phoneNumber, password, isAdmin, is_super):
        self.config = database_configuration()
        self.firstname = firstname
        self.lastname = lastname
        self.othername = othername
        self.username = username
        self.email = email
        self.phoneNumber = phoneNumber
        self.password = generate_password_hash(password)
        self.isAdmin = isAdmin
        self.is_super = is_super  

    def add_user(self):
        con, response = psycopg2.connect(**self.config), None
        cur = con.cursor(cursor_factory=RealDictCursor)
        try:
            query = "INSERT INTO users(firstname,lastname,othername,username,email,phoneNumber,password,isAdmin,is_super) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s) RETURNING *; "
            cur.execute(query, (
                self.firstname, 
                self.lastname,
                self.othername,
                self.username,
                self.email,
                self.phoneNumber,
                self.password,
                self.isAdmin,
                self.is_super
            ))
            con.commit()
            response = cur.fetchone()
        except Exception as e:
            con.close()
        con.close()
        return response

    @staticmethod
    def get_all_users():
        config = database_configuration()
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
        config = database_configuration()
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
    def update_user(is_admin, normal_user_id):
        config = database_configuration()
        con, response = psycopg2.connect(**config), None
        cur = con.cursor(cursor_factory=RealDictCursor)
        try:
            query = "UPDATE users SET isadmin=%s WHERE id=%s;"
            cur.execute(query, (
                is_admin, 
                normal_user_id
            ))
            con.commit()
            response = True
        except Exception as e:
            con.close()
            response = False
        con.close()
        return response

    @staticmethod
    def get_super(user_id):
        user = UserInfo.get_one_user(user_id)
        if user['is_super'] == True:
            return True
        return False
    