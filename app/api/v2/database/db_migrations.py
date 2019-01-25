'''
Database migrations allow us to:
Recreate a database from scratch
Make it clear at all times what state a database is in
Migrate in a deterministic way from your current version of the database to a newer one
Kind of like git
'''
from flask import current_app
from app.api.v2.database.db import create_tables_command
from app.api.v2.database.drop_table import drop_tables_command
import psycopg2
import psycopg2.extras
from app.api.v2.database.db_configs import database_configuration

class Database:
    def __init__(self):
        self.config = database_configuration()

    def migrations(self):
        connection = psycopg2.connect(**self.config)
        #commit changes after db transaction
        connection.autocommit = True
        #cursor can access the connection object
        #cursors encapsulate queries and executes them stepwise
        #This helps me reference columns in the table by name
        cur_con = connection.cursor(cursor_factory=psycopg2.extras.DictCursor)
        database = self.config.get('database')
        #check if databases exists
        cur_con.execute("select * from pg_database where datname = %(database_name)s", {'database_name': database})
        dbs = cur_con.fetchall()
        if len(dbs) > 0:
            print(" * Database {} exists".format(database))
            #if the database exists, the tables are created
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