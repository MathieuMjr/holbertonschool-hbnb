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

# class TestPlaceEndpoints(unittest.TestCase):

    # def setUp(self):
    #     self.app = create_app()
    #     self.client = self.app.test_client()

    # def test_create_place(self):
    #     response = self.client.post('/api/v1/users/', json={
    #         "first_name": "Jane",
    #         "last_name": "Doe",
    #         "email": "jane.doe@example.com"
    #     })
    #     self.assertEqual(response.status_code, 201)

    # def test_create_user_invalid_data(self):
    #     response = self.client.post('/api/v1/users/', json={
    #         "first_name": "",
    #         "last_name": "",
    #         "email": "invalid-email"
    #     })
    #     self.assertEqual(response.status_code, 400)
