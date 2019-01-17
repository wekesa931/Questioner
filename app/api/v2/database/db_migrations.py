from flask import current_app
from app.api.v2.database.db import create_tables_command
import psycopg2
import psycopg2.extras
import os
from urllib.parse import urlparse

class Database:
    def __init__(self):
        self.db_config = os.getenv('api_database_url')

    def migrations(self):
        response = urlparse(self.db_config)
        config = {
            'database': response.path[1:],
            'user': response.username,
            'password': '',
            'host': response.hostname
        }
        connection = psycopg2.connect(**config)
        connection.autocommit = True
        cur_con = connection.cursor(cursor_factory=psycopg2.extras.DictCursor)
        database = config.get('database')
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

db = Database()