import psycopg2
import os
from pprint import pprint


class DatabaseConnection:  
    def __init__(self):
        try:
            postgresdb = 'swett'
            Host="localhost"
            User="postgres"
            Password="test"

            if os.getenv('env') == "testing":
                postgresdb = 'fasters'
                Host="localhost"
                User="postgres"
                Password= "test"

            self.connection = psycopg2.connect(
                    database=postgresdb, host=Host, user=User,
                    password=Password, port="5432"
                )
            self.connection.autocommit = True
            self.cursor = self.connection.cursor()
        except:
            pprint('cannot connect to database')

    def create_user_table(self):
        create_table = """CREATE TABLE IF NOT EXISTS users(
            userId SERIAL PRIMARY KEY,
            username VARCHAR UNIQUE,
            email VARCHAR,
            password VARCHAR,
            role VARCHAR)"""
        self.cursor.execute(create_table)
        self.connection.commit()

    

database = DatabaseConnection()
database.create_user_table()