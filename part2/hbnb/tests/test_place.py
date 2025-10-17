from app.models.place import Place
from app.models.user import User
from app.models.review import Review
import unittest
from app import create_app


def test_place_creation():
    owner = User(
        first_name="Alice", last_name="Smith", email="alice.smith@example.com")
    place = Place(
        title="Cozy Apartment",
        description="A nice place to stay",
        price=100,
        latitude=37.7749,
        longitude=-122.4194,
        owner_id=owner,
    )

    # Adding a review
    review = Review(
        comment="Great stay!", rating=5, place_id=place, user_id=owner)
    place.add_review(review)

    assert place.title == "Cozy Apartment"
    assert place.price == 100
    assert len(place.reviews) == 1
    assert place.reviews[0].comment == "Great stay!"
    print("Place creation and relationship test passed!")


test_place_creation()

# --- UNITTEST - API


class TestPlaceEndpoints(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()

    def test_place_create(self):
        user_1 = {
            "first_name": "Infinite",
            "last_name": "Minion",
            "email": "minion11@example.com"
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

    def test_place_create_bad_lat(self):
        user_1 = {
            "first_name": "Infinite",
            "last_name": "Minion",
            "email": "minion12@example.com"
            }
        response = self.client.post('/api/v1/users/', json=user_1)
        self.assertEqual(response.status_code, 201)
        user_id = response.json['id']

        place_1 = {
            "title": "Pretty Apartment",
            "description": "A lovely place to stay",
            "price": 200.0,
            "latitude": 91,
            "longitude": -122.4194,
            "owner_id": f"{user_id}"
            }
        response = self.client.post('/api/v1/places/', json=place_1)
        self.assertEqual(response.status_code, 400)

    def test_place_create_bad_long(self):
        user_1 = {
            "first_name": "Infinite",
            "last_name": "Minion",
            "email": "minion13@example.com"
            }
        response = self.client.post('/api/v1/users/', json=user_1)
        self.assertEqual(response.status_code, 201)
        user_id = response.json['id']

        place_1 = {
            "title": "Pretty Apartment",
            "description": "A lovely place to stay",
            "price": 200.0,
            "latitude": 50.7749,
            "longitude": -181,
            "owner_id": f"{user_id}"
            }
        response = self.client.post('/api/v1/places/', json=place_1)
        self.assertEqual(response.status_code, 400)

    def test_place_create_bad_price(self):
        user_1 = {
            "first_name": "Infinite",
            "last_name": "Minion",
            "email": "minion14@example.com"
            }
        response = self.client.post('/api/v1/users/', json=user_1)
        self.assertEqual(response.status_code, 201)
        user_id = response.json['id']

        place_1 = {
            "title": "Pretty Apartment",
            "description": "A lovely place to stay",
            "price": 0,
            "latitude": 50.7749,
            "longitude": -122.4194,
            "owner_id": f"{user_id}"
            }
        response = self.client.post('/api/v1/places/', json=place_1)
        self.assertEqual(response.status_code, 400)

    def test_place_create_bad_owner(self):
        user_1 = {
            "first_name": "Infinite",
            "last_name": "Minion",
            "email": "minion15@example.com"
            }
        response = self.client.post('/api/v1/users/', json=user_1)
        self.assertEqual(response.status_code, 201)
        user_id = "JOKE"

        place_1 = {
            "title": "Pretty Apartment",
            "description": "A lovely place to stay",
            "price": 200.0,
            "latitude": 50.7749,
            "longitude": -122.4194,
            "owner_id": f"{user_id}"
            }
        response = self.client.post('/api/v1/places/', json=place_1)
        self.assertEqual(response.status_code, 404)

    def test_get_all(self):
        response = self.client.get('/api/v1/places/', json={})
        self.assertEqual(response.status_code, 200)

    def test_get_by_id(self):
        user_1 = {
            "first_name": "Infinite",
            "last_name": "Minion",
            "email": "minion16@example.com"
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

        response = self.client.get(f'/api/v1/places/{place_id}', json={})
        self.assertEqual(response.status_code, 200)

    def test_get_by_bad_id(self):
        user_1 = {
            "first_name": "Infinite",
            "last_name": "Minion",
            "email": "minion17@example.com"
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
        place_id = "trolled"

        response = self.client.get(f'/api/v1/places/{place_id}', json={})
        self.assertEqual(response.status_code, 404)

    def test_update(self):
        user_1 = {
            "first_name": "Infinite",
            "last_name": "Minion",
            "email": "minion18@example.com"
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

        update_datas = {
            "title": "CHOOSE MY PLACE",
            "description": ":o",
            "price": 100.0,
            "latitude": 78.250,
            "longitude": 179.0,
        }
        response = self.client.post('/api/v1/places/', json=place_1)
        self.assertEqual(response.status_code, 201)
        place_id = response.json['id']

        response = self.client.put(
            f'/api/v1/places/{place_id}', json=update_datas)
        self.assertEqual(response.status_code, 200)

    def test_update_bad_id(self):
        user_1 = {
            "first_name": "Infinite",
            "last_name": "Minion",
            "email": "minion19@example.com"
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

        update_datas = {
            "title": "CHOOSE MY PLACE",
            "description": ":o",
            "price": 100.0,
            "latitude": 78.250,
            "longitude": 179.0,
        }
        response = self.client.post('/api/v1/places/', json=place_1)
        self.assertEqual(response.status_code, 201)
        place_id = "@_@"

        response = self.client.put(
            f'/api/v1/places/{place_id}', json=update_datas)
        self.assertEqual(response.status_code, 404)

    def test_update_bad_lat(self):
        user_1 = {
            "first_name": "Infinite",
            "last_name": "Minion",
            "email": "minion20@example.com"
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

        update_datas = {
            "title": "CHOOSE MY PLACE",
            "description": ":o",
            "price": 100.0,
            "latitude": 91,
            "longitude": 179.0,
        }
        response = self.client.post('/api/v1/places/', json=place_1)
        self.assertEqual(response.status_code, 201)
        place_id = response.json['id']

        response = self.client.put(
            f'/api/v1/places/{place_id}', json=update_datas)
        self.assertEqual(response.status_code, 400)

    def test_update_bad_long(self):
        user_1 = {
            "first_name": "Infinite",
            "last_name": "Minion",
            "email": "minion21@example.com"
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

        update_datas = {
            "title": "CHOOSE MY PLACE",
            "description": ":o",
            "price": 100.0,
            "latitude": 78.250,
            "longitude": -181.0,
        }
        response = self.client.post('/api/v1/places/', json=place_1)
        self.assertEqual(response.status_code, 201)
        place_id = response.json['id']

        response = self.client.put(
            f'/api/v1/places/{place_id}', json=update_datas)
        self.assertEqual(response.status_code, 400)

    def test_update_bad_price(self):
        user_1 = {
            "first_name": "Infinite",
            "last_name": "Minion",
            "email": "minion22@example.com"
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

        update_datas = {
            "title": "CHOOSE MY PLACE",
            "description": ":o",
            "price": -100.2,
            "latitude": 78.250,
            "longitude": 179.0,
        }
        response = self.client.post('/api/v1/places/', json=place_1)
        self.assertEqual(response.status_code, 201)
        place_id = response.json['id']

        response = self.client.put(
            f'/api/v1/places/{place_id}', json=update_datas)
        self.assertEqual(response.status_code, 400)

    def test_get_place_reviews(self):
        user_1 = {
            "first_name": "Infinite",
            "last_name": "Minion",
            "email": "minion23@example.com"
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
        review_2 = {
            "comment": "Wololo... SO COOL",
            "rating": 1,
            "place_id": f"{place_id}",
            "user_id": f"{user_id}"
        }
        response = self.client.post('/api/v1/reviews/', json=review_2)
        self.assertEqual(response.status_code, 201)

        response = self.client.get(
            f'/api/v1/places/{place_id}/reviews')
        self.assertEqual(response.status_code, 200)

    def test_get_place_reviews_bad_id(self):
        user_1 = {
            "first_name": "Infinite",
            "last_name": "Minion",
            "email": "minion24@example.com"
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
        review_2 = {
            "comment": "Wololo... SO COOL",
            "rating": 1,
            "place_id": f"{place_id}",
            "user_id": f"{user_id}"
        }
        response = self.client.post('/api/v1/reviews/', json=review_2)
        self.assertEqual(response.status_code, 201)

        place_id = "NO ID"
        response = self.client.get(
            f'/api/v1/places/{place_id}/reviews')
        self.assertEqual(response.status_code, 404)
