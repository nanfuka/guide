"""This file handles setting up the connection to database"""
import os
import psycopg2
import psycopg2.extras as sendIT


class Database:
    """This class connects to the database"""

    def __init__(self):
        db_name = "swett"

        self.conn = psycopg2.connect(
            database=db_name, user="postgres", password="test",
            port="5432"
        )
        self.conn.autocommit = True
        self.cur = self.conn.cursor(cursor_factory=sendIT.RealDictCursor)

        create_user_table = """CREATE TABLE IF NOT EXISTS users(
                user_id SERIAL PRIMARY KEY,
                username VARCHAR NOT NULL,
                email VARCHAR NOT NULL,
                password VARCHAR NOT NULL,
                role VARCHAR NOT NULL
            )"""

        self.cur.execute(create_user_table)

    def create_tables(self):
        """method for creating all tables"""
        create_user_table = """CREATE TABLE IF NOT EXISTS users(
                user_id SERIAL PRIMARY KEY,
                username VARCHAR NOT NULL,
                email VARCHAR NOT NULL,
                password VARCHAR NOT NULL,
                role VARCHAR NOT NULL
            )"""
       
        commands = (
            create_user_table
        )

        for command in commands:
            self.cur.execute(command)

    def drop_table(self, *table_names):
        '''Drops the tables created '''
        for table_name in table_names:
            drop_table = "DROP TABLE IF EXISTS {} CASCADE".format(table_name)
            self.cur.execute(drop_table)