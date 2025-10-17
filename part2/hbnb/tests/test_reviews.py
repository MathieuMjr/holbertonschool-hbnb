import unittest
from app import create_app

# --- UNITTEST - API


class TestAmenityEndpoints(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()

    def test_review_create(self):
        user_1 = {
            "first_name": "Sarah",
            "last_name": "Croche",
            "email": "dringdring@example.com"
        }
        response = self.client.post('/api/v1/users/', json=user_1)
        self.assertEqual(response.status_code, 201)
        user_id = response.json['id']

        place_1 = {
            "title": "Pretty Apartment",
            "description": "A lovely place to stay",
            "price": 200.0,
            "latitude": 50.7749,
            "longitude": -122.4194,
            "owner_id": f"{user_id}"
            }
        response = self.client.post('/api/v1/places/', json=place_1)
        self.assertEqual(response.status_code, 201)
        place_id = response.json['id']

        review_1 = {
            "comment": "Great palce to stay!",
            "rating": 5,
            "place_id": f"{place_id}",
            "user_id": f"{user_id}"
        }
        response = self.client.post('/api/v1/reviews/', json=review_1)
        self.assertEqual(response.status_code, 201)

    def test_review_create_bad_rating(self):
        user_1 = {
            "first_name": "Infinite",
            "last_name": "Minion",
            "email": "minion1@example.com"
        }
        response = self.client.post('/api/v1/users/', json=user_1)
        self.assertEqual(response.status_code, 201)
        user_id = response.json['id']

        place_1 = {
            "title": "Pretty Apartment",
            "description": "A lovely place to stay",
            "price": 200.0,
            "latitude": 50.7749,
            "longitude": -122.4194,
            "owner_id": f"{user_id}"
            }
        response = self.client.post('/api/v1/places/', json=place_1)
        self.assertEqual(response.status_code, 201)
        place_id = response.json['id']

        review_1 = {
            "comment": "Great palce to stay!",
            "rating": 1000,
            "place_id": f"{place_id}",
            "user_id": f"{user_id}"
        }
        response = self.client.post('/api/v1/reviews/', json=review_1)
        self.assertEqual(response.status_code, 400)

    def test_review_create_bad_place_id(self):
        user_1 = {
            "first_name": "Infinite",
            "last_name": "Minion",
            "email": "minion2@example.com"
        }
        response = self.client.post('/api/v1/users/', json=user_1)
        self.assertEqual(response.status_code, 201)
        user_id = response.json['id']

        place_1 = {
            "title": "Pretty Apartment",
            "description": "A lovely place to stay",
            "price": 200.0,
            "latitude": 50.7749,
            "longitude": -122.4194,
            "owner_id": f"{user_id}"
            }
        response = self.client.post('/api/v1/places/', json=place_1)
        self.assertEqual(response.status_code, 201)
        place_id = "oh noOOOOoOOOo"

        review_1 = {
            "comment": "Great palce to stay!",
            "rating": 5,
            "place_id": f"{place_id}",
            "user_id": f"{user_id}"
        }
        response = self.client.post('/api/v1/reviews/', json=review_1)
        self.assertEqual(response.status_code, 404)

    def test_review_create_bad_user_id(self):
        user_1 = {
            "first_name": "Infinite",
            "last_name": "Minion",
            "email": "minion3@example.com"
        }
        response = self.client.post('/api/v1/users/', json=user_1)
        self.assertEqual(response.status_code, 201)
        user_id = response.json['id']

        place_1 = {
            "title": "Pretty Apartment",
            "description": "A lovely place to stay",
            "price": 200.0,
            "latitude": 50.7749,
            "longitude": -122.4194,
            "owner_id": f"{user_id}"
            }
        response = self.client.post('/api/v1/places/', json=place_1)
        self.assertEqual(response.status_code, 201)
        place_id = response.json['id']

        user_id = "bruhu"  # turn user id into a fake one after place
        # successfully created with true ID
        review_1 = {
            "comment": "Great palce to stay!",
            "rating": 5,
            "place_id": f"{place_id}",
            "user_id": f"{user_id}"
        }
        response = self.client.post('/api/v1/reviews/', json=review_1)
        self.assertEqual(response.status_code, 404)

    def test_get_all(self):
        response = self.client.get('/api/v1/reviews/', json={})
        self.assertEqual(response.status_code, 200)

    def test_get_by_id(self):
        user_1 = {
            "first_name": "Infinite",
            "last_name": "Minion",
            "email": "minion4@example.com"
            }
        response = self.client.post('/api/v1/users/', json=user_1)
        self.assertEqual(response.status_code, 201)
        user_id = response.json['id']

        place_1 = {
            "title": "Pretty Apartment",
            "description": "A lovely place to stay",
            "price": 200.0,
            "latitude": 50.7749,
            "longitude": -122.4194,
            "owner_id": f"{user_id}"
            }
        response = self.client.post('/api/v1/places/', json=place_1)
        self.assertEqual(response.status_code, 201)
        place_id = response.json['id']

        review_1 = {
            "comment": "Great palce to stay!",
            "rating": 5,
            "place_id": f"{place_id}",
            "user_id": f"{user_id}"
        }
        response = self.client.post('/api/v1/reviews/', json=review_1)
        self.assertEqual(response.status_code, 201)
        review_id = response.json['id']

        response = self.client.get(f'/api/v1/reviews/{review_id}')
        self.assertEqual(response.status_code, 200)

    def test_get_by_bad_id(self):
        user_1 = {
            "first_name": "Infinite",
            "last_name": "Minion",
            "email": "minion5@example.com"
            }
        response = self.client.post('/api/v1/users/', json=user_1)
        self.assertEqual(response.status_code, 201)
        user_id = response.json['id']

        place_1 = {
            "title": "Pretty Apartment",
            "description": "A lovely place to stay",
            "price": 200.0,
            "latitude": 50.7749,
            "longitude": -122.4194,
            "owner_id": f"{user_id}"
            }
        response = self.client.post('/api/v1/places/', json=place_1)
        self.assertEqual(response.status_code, 201)
        place_id = response.json['id']

        review_1 = {
            "comment": "Great palce to stay!",
            "rating": 5,
            "place_id": f"{place_id}",
            "user_id": f"{user_id}"
        }
        response = self.client.post('/api/v1/reviews/', json=review_1)
        self.assertEqual(response.status_code, 201)
        review_id = "hoyaaaaah"

        response = self.client.get(f'/api/v1/reviews/{review_id}')
        self.assertEqual(response.status_code, 404)

    def test_delete(self):
        user_1 = {
            "first_name": "Infinite",
            "last_name": "Minion",
            "email": "minion6@example.com"
            }
        response = self.client.post('/api/v1/users/', json=user_1)
        self.assertEqual(response.status_code, 201)
        user_id = response.json['id']

        place_1 = {
            "title": "Pretty Apartment",
            "description": "A lovely place to stay",
            "price": 200.0,
            "latitude": 50.7749,
            "longitude": -122.4194,
            "owner_id": f"{user_id}"
            }
        response = self.client.post('/api/v1/places/', json=place_1)
        self.assertEqual(response.status_code, 201)
        place_id = response.json['id']

        review_1 = {
            "comment": "Great palce to stay!",
            "rating": 5,
            "place_id": f"{place_id}",
            "user_id": f"{user_id}"
        }
        response = self.client.post('/api/v1/reviews/', json=review_1)
        self.assertEqual(response.status_code, 201)
        review_id = response.json['id']

        response = self.client.delete(f'/api/v1/reviews/{review_id}')
        self.assertEqual(response.status_code, 200)

    def test_delete_bad_id(self):
        user_1 = {
            "first_name": "Infinite",
            "last_name": "Minion",
            "email": "minion7@example.com"
            }
        response = self.client.post('/api/v1/users/', json=user_1)
        self.assertEqual(response.status_code, 201)
        user_id = response.json['id']

        place_1 = {
            "title": "Pretty Apartment",
            "description": "A lovely place to stay",
            "price": 200.0,
            "latitude": 50.7749,
            "longitude": -122.4194,
            "owner_id": f"{user_id}"
            }
        response = self.client.post('/api/v1/places/', json=place_1)
        self.assertEqual(response.status_code, 201)
        place_id = response.json['id']

        review_1 = {
            "comment": "Great palce to stay!",
            "rating": 5,
            "place_id": f"{place_id}",
            "user_id": f"{user_id}"
        }
        response = self.client.post('/api/v1/reviews/', json=review_1)
        self.assertEqual(response.status_code, 201)
        review_id = "supercalifragilisticexpialidocious"

        response = self.client.delete(f'/api/v1/reviews/{review_id}')
        self.assertEqual(response.status_code, 404)

    def test_update(self):
        user_1 = {
            "first_name": "Infinite",
            "last_name": "Minion",
            "email": "minion8@example.com"
            }
        response = self.client.post('/api/v1/users/', json=user_1)
        self.assertEqual(response.status_code, 201)
        user_id = response.json['id']

        place_1 = {
            "title": "Pretty Apartment",
            "description": "A lovely place to stay",
            "price": 200.0,
            "latitude": 50.7749,
            "longitude": -122.4194,
            "owner_id": f"{user_id}"
            }
        response = self.client.post('/api/v1/places/', json=place_1)
        self.assertEqual(response.status_code, 201)
        place_id = response.json['id']

        review_1 = {
            "comment": "Great palce to stay!",
            "rating": 5,
            "place_id": f"{place_id}",
            "user_id": f"{user_id}"
        }

        update_datas = {
            "comment": "Wololo... SO COOL",
            "rating": 1
        }
        response = self.client.post('/api/v1/reviews/', json=review_1)
        self.assertEqual(response.status_code, 201)
        review_id = response.json['id']

        response = self.client.put(
            f'/api/v1/reviews/{review_id}', json=update_datas)
        self.assertEqual(response.status_code, 200)

    def test_update_bad_id(self):
        user_1 = {
            "first_name": "Infinite",
            "last_name": "Minion",
            "email": "minion9@example.com"
            }
        response = self.client.post('/api/v1/users/', json=user_1)
        self.assertEqual(response.status_code, 201)
        user_id = response.json['id']

        place_1 = {
            "title": "Pretty Apartment",
            "description": "A lovely place to stay",
            "price": 200.0,
            "latitude": 50.7749,
            "longitude": -122.4194,
            "owner_id": f"{user_id}"
            }
        response = self.client.post('/api/v1/places/', json=place_1)
        self.assertEqual(response.status_code, 201)
        place_id = response.json['id']

        review_1 = {
            "comment": "Great palce to stay!",
            "rating": 5,
            "place_id": f"{place_id}",
            "user_id": f"{user_id}"
        }

        update_datas = {
            "comment": "Wololo... SO COOL",
            "rating": 1
        }
        response = self.client.post('/api/v1/reviews/', json=review_1)
        self.assertEqual(response.status_code, 201)
        review_id = "like...again ?!"

        response = self.client.put(
            f'/api/v1/reviews/{review_id}', json=update_datas)
        self.assertEqual(response.status_code, 404)

    def test_update_bad_value(self):
        user_1 = {
            "first_name": "Infinite",
            "last_name": "Minion",
            "email": "minion10@example.com"
            }
        response = self.client.post('/api/v1/users/', json=user_1)
        self.assertEqual(response.status_code, 201)
        user_id = response.json['id']

        place_1 = {
            "title": "Pretty Apartment",
            "description": "A lovely place to stay",
            "price": 200.0,
            "latitude": 50.7749,
            "longitude": -122.4194,
            "owner_id": f"{user_id}"
            }
        response = self.client.post('/api/v1/places/', json=place_1)
        self.assertEqual(response.status_code, 201)
        place_id = response.json['id']

        review_1 = {
            "comment": "Great palce to stay!",
            "rating": 5,
            "place_id": f"{place_id}",
            "user_id": f"{user_id}"
        }

        update_datas = {
            "comment": "Wololo... SO COOL",
            "rating": -2
        }
        response = self.client.post('/api/v1/reviews/', json=review_1)
        self.assertEqual(response.status_code, 201)
        review_id = response.json['id']

        response = self.client.put(
            f'/api/v1/reviews/{review_id}', json=update_datas)
        self.assertEqual(response.status_code, 400)
