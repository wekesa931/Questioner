from flask import current_app
from app.api.v2.database.db import create_tables_command
from app.api.v2.database.drop_table import drop_tables_command
import psycopg2
#holds function helpers
import psycopg2.extras
import os
from urllib.parse import urlparse

class Database:
    def __init__(self):
        self.db_config = os.getenv('api_database_url')
        #break down the URL into parts
        self.response = urlparse(self.db_config)
        self.config = {
            'database': self.response.path[1:],
            'user': self.response.username,
            'password': '',
            'host': self.response.hostname
        }

    def migrations(self):
        connection = psycopg2.connect(**self.config)
        #commit changes after db transaction
        connection.autocommit = True
        #cursor can access the connection object
        #cursors encapsulate queries and executes them stepwise
        cur_con = connection.cursor(cursor_factory=psycopg2.extras.DictCursor)
        database = self.config.get('database')
        cur_con.execute("select * from pg_database where datname = %(database_name)s", {'database_name': database})
        dbs = cur_con.fetchall()
        if len(dbs) > 0:
            print(" * Database {} exists".format(database))
            for command in create_tables_command:
                cur_con.execute(command)
                connection.commit()
        else:
            print(" * Database {} does not exists".format(database))
        connection.close()

    def drop_tables(self):
        connection = psycopg2.connect(**self.config)
        connection.autocommit = True
        cur_con = connection.cursor(cursor_factory=psycopg2.extras.DictCursor)
        database = self.config.get('database')
        cur_con.execute("select * from pg_database where datname = %(database_name)s", {'database_name': database})
        dbs = cur_con.fetchall()
        if len(dbs) > 0:
            print(" * Database {} exists".format(database))
            for command in drop_tables_command:
                cur_con.execute(command)
                connection.commit()
        else:
            print(" * Database {} does not exists".format(database))
        connection.close()


db = Database()