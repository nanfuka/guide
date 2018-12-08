# import unittest
# from app.views import app
# import json
# from db import DatabaseConnection

# db = DatabaseConnection()


# class TestUsers(unittest.TestCase):
#     def setUp(self):
#         self.test_client = app.test_client(self)

#     def test_user_register(self):
#         user = {
#             'username': 'kengowadaty',
#             'email': 'kengoty@email.com',
#             'password': 'kengowada',
#             'role': 'admin'
#         }

#         response = self.test_client.post(
#             'api/v1/signup',
#             content_type='application/json',
#             data=json.dumps(user)
#         )
#         message = json.loads(response.data.decode())

#         self.assertEqual(response.status_code, 403)

from app.views import app
from db import DatabaseConnection
import unittest
import json
from tests.getToken import GetToken
 

class AppTestCase(unittest.TestCase):
    def setUp(self):
        """Initialisez app and defines variables"""
        app.testing = True
        self.tester = app.test_client()
        self.database = DatabaseConnection()
        self.database.create_user_table()

        self.user = {
            'username': '', 'email': 'joshua@gmail.com',
            'password': 'yes', 'role': 'user'
            }

    def tearDown(self):
        """Crashes down all initialized variables"""

        self.database.cursor.execute("DROP TABLE users")
        self.tester = None

    def test_user_register(self):
        user = {
            'username': 'kengowadaty',
            'email': 'kengoty@email.com',
            'password': 'kengowada',
            'role':'user'
        }
        response = self.tester.post(
            'api/v1/signup',
            content_type='application/json',
            data=json.dumps(user)
        )
        message = json.loads(response.data.decode())

        self.assertEqual(201, response.status_code)
        self.assertIn("you have succesfully signed up", str(response.data))
    # def test_create_user(self):
    #     """create a new user"""
    #     response = self.tester.post('/api/v1/signup', data=self.user)
    #     self.assertEqual(201, response.status_code)
    #     self.assertIn('User created successfully', str(response.data))

    #     """test sign up with special characters"""
    #     response = self.tester.post('/api/v1/auth/signup', data={
    #         'username': '$@joshua', 'email': 'joshua@gmail.com',
    #         'password': 'yes'
    #     })
    #     self.assertEqual(400, response.status_code)
    #     self.assertIn('username cannot have special characters', str(response.data))

    #     """test sign up username conflict"""
    #     response = self.tester.post('/api/v1/auth/signup', data={
    #         'username': 'joshua', 'email': 'joshua@gmail.com',
    #         'password': 'yes'
    #     })
    #     self.assertEqual(409, response.status_code)
    #     self.assertIn('user already exists', str(response.data))

    #     """test sign up with email conflict"""
    #     response = self.tester.post('/api/v1/auth/signup', data={
    #         'username': 'dan', 'email': 'joshua@gmail.com',
    #         'password': 'yes'
    #     })
    #     self.assertEqual(409, response.status_code)
    #     self.assertIn('please use another email address', str(response.data))

    #     """test spaced username in sign up"""
    #     response = self.tester.post('/api/v1/auth/signup', data={
    #         'username': '  ', 'email': 'dan@gmail.com',
    #         'password': 'yes'
    #     })
    #     self.assertEqual(400, response.status_code)
    #     self.assertIn('Field cannot be blank', str(response.data))

    #     """test invalid email format"""
    #     response = self.tester.post('/api/v1/auth/signup', data={
    #         'username': 'dan', 'email': 'daniel',
    #         'password': 'yes'
    #     })
    #     self.assertEqual(400, response.status_code)
    #     self.assertIn('Invalid email', str(response.data))

    # def test_login_user(self):
    #     """tests api for user login"""
    #     response = self.tester.post('/api/v1/auth/signup', data=self.user)
    #     self.assertEqual(201, response.status_code)
    #     self.assertIn('User created successfully', str(response.data))
    #     response = self.tester.post('/api/v1/auth/login', data=self.user)
    #     self.assertEqual(200, response.status_code)
    #     self.assertIn('You are successfully logged in', str(response.data))

    #     """test login for non existing user"""
    #     response = self.tester.post('/api/v1/auth/login', data={
    #         'username': 'lugada', 'email': 'lugada@gmail.com',
    #         'password': 'yes'
    #     })
    #     self.assertEqual(401, response.status_code)
    #     self.assertIn('Please Create an account', str(response.data))

    #     """test login with incorrect credentials"""
    #     response = self.tester.post('/api/v1/auth/login', data={
    #         'username': 'joshua', 'password': 'yes456'
    #     })
    #     self.assertEqual(401, response.status_code)
    #     self.assertIn('username or password is incorrect', str(response.data))

    # def test_admin_signin(self):
    #     """tests api for admin login"""
    #     response = self.tester.post('/api/v1/auth/login', data={
    #         'username': 'admin',
    #         'password': 'mynameisadmin'})
    #     self.assertEqual(200, response.status_code)
    #     self.assertIn('welcome admin', str(response.data))