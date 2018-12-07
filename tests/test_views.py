import unittest
from app.views import app
import json
from db import DatabaseConnection

db = DatabaseConnection()


class TestUsers(unittest.TestCase):
    def setUp(self):
        self.test_client = app.test_client(self)

    def test_user_register(self):
        user = {
            'username': 'kengowadaty',
            'email': 'kengoty@email.com',
            'password': 'kengowada',
            'role': 'admin'
        }

        response = self.test_client.post(
            'api/v1/signup',
            content_type='application/json',
            data=json.dumps(user)
        )
        message = json.loads(response.data.decode())

        self.assertEqual(response.status_code, 403)
