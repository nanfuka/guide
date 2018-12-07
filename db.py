import psycopg2
from pprint import pprint
import os


class DatabaseConnection:

    def __init__(self):
        # if os.getenv('APP_SETTINGS') == 'test_db':
        #     self.db = 'test_db'
        # else:
        #     self.db = 'stackoverflow'

        try:
            self.connection = psycopg2.connect(
                dbname='swett', user='postgres',  password='test', port='5432'
            )

            self.connection.autocommit = True
            self.cursor = self.connection.cursor()

            pprint('Database connected.')
            create_user_table = "CREATE TABLE IF NOT EXISTS users (userId SERIAL PRIMARY KEY, username TEXT NOT NULL, email TEXT NOT NULL, password TEXT NOT NULL, role TEXT NOT NULL);"

            self.cursor.execute(create_user_table)

        except:
            pprint('Cannot connect to the database.')

    # def insert_users(self, userId, username, email, password):
    #     insert_user = "INSERT INTO users(userId, username, email, password) VALUES('{}', '{}', '{}', '{}')".format(
    #         userId, username, email, password)
    #     pprint(insert_user)
    #     self.cursor.execute(insert_user)


    # def login(self, username):
    #     query = "SELECT * FROM users WHERE username='{}'".format(username)
    #     pprint(query)
    #     self.cursor.execute(query)
    #     user = self.cursor.fetchone()
    #     return user

    # def user(self, username):
    #     query = "SELECT username FROM users WHERE username='{}'".format(
    #         username)
    #     pprint(query)
    #     self.cursor.execute(query)
    #     userId = self.cursor.fetchone()
    #     return userId

    # def check_password(self, password):
    #     query = "SELECT password FROM users WHERE password='{}'".format(
    #         password)
    #     pprint(query)
    #     self.cursor.execute(query)
    #     userId = self.cursor.fetchone()
    #     return userId

    # def check_username(self, username):
    #     query = "SELECT username FROM users WHERE username='{}'".format(
    #         username)
    #     pprint(query)
    #     self.cursor.execute(query)
    #     user = self.cursor.fetchone()
    #     return user

    # def check_email(self, email):
    #     query = "SELECT email FROM users WHERE email='{}'".format(email)
    #     pprint(query)
    #     self.cursor.execute(query)
    #     email = self.cursor.fetchone()
    #     return email

    def drop_tables(self):
        drop = "DROP TABLE users"
        pprint(drop)
        self.cursor.execute(drop)


if __name__ == '__main__':
    database_connection = DatabaseConnection()