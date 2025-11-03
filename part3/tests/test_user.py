from app.models.user import User
import unittest
from app import create_app


# def test_user_creation():
#     user = User(
#         first_name="John", last_name="Doe", email="john.doe@example.com", password='secret')
#     assert user.first_name == "John"
#     assert user.last_name == "Doe"
#     assert user.email == "john.doe@example.com"
#     assert user.is_admin is False  # Default value
#     print("User creation test passed!")


# test_user_creation()

# --- UNITTEST - API ----------------------------------------------------


class TestUserEndpoints(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()

    def test_create_user(self):
        user_1 = {
            "first_name": "Jane",
            "last_name": "Doe",
            "email": "jane.doe@example.com"
        }
        response = self.client.post('/api/v1/users/', json=user_1)
        self.assertEqual(response.status_code, 201)

    def test_create_user_invalid_data(self):
        response = self.client.post('/api/v1/users/', json={
            "first_name": "",
            "last_name": "",
            "email": "invalid-email"
        })
        self.assertEqual(response.status_code, 400)

    def test_update_user(self):
        user2 = {
            "first_name": "John",
            "last_name": "Doe",
            "email": "john.doe@example.com"
        }
        user2_update = {
            "first_name": "John",
            "last_name": "Doe",
            "email": "john2.doe@example.com"
        }

        response_user2 = self.client.post('/api/v1/users/', json=user2)
        self.assertEqual(response_user2.status_code, 201)
        user2_id = response_user2.json['id']

        response_user2_update = self.client.put(
            f'api/v1/users/{user2_id}', json=user2_update)
        self.assertEqual(response_user2_update.status_code, 200)

    def test_update_user_email_exist(self):
        user_3 = {
            "first_name": "Jean-Michel",
            "last_name": "Apeuprès",
            "email": "mimi@example.com"
        }
        user2_update = {
            "first_name": "JM",
            "last_name": "Malsapé",
            "email": "jane.doe@example.com"
        }
        response = self.client.post('/api/v1/users/', json=user_3)
        self.assertEqual(response.status_code, 201)
        user3_id = response.json['id']

        response_user2_update = self.client.put(
            f'api/v1/users/{user3_id}', json=user2_update)
        self.assertEqual(response_user2_update.status_code, 400)

    def test_get_by_id(self):
        user4 = {
            "first_name": "Gisèle",
            "last_name": "Troncoup",
            "email": "gigi@example.com"
        }
        response = self.client.post('/api/v1/users/', json=user4)
        self.assertEqual(response.status_code, 201)
        user4_id = response.json['id']
        response = self.client.get(f'/api/v1/users/{user4_id}', json={})
        self.assertEqual(response.status_code, 200)

    def test_get_by_bad_id(self):
        user5 = {
            "first_name": "Charles",
            "last_name": "Fevrier",
            "email": "chacha@example.com"
        }
        response = self.client.post('/api/v1/users/', json=user5)
        self.assertEqual(response.status_code, 201)
        fake_id = "tralalala"
        response = self.client.get(f'/api/v1/users/{fake_id}', json={})
        self.assertEqual(response.status_code, 404)

    def get_all(self):
        response = self.client.get('/api/v1/users/', json={})
        self.assertEqual(response.status_code, 200)
