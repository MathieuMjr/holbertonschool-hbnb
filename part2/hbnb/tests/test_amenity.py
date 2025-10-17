from app.models.amenity import Amenity
import unittest
from app import create_app


def test_amenity_creation():
    amenity = Amenity(name="Wi-Fi")
    assert amenity.name == "Wi-Fi"
    print("Amenity creation test passed!")


test_amenity_creation()

# --- UNITTEST - API


class TestAmenityEndpoints(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()

    def test_create_amenity(self):
        amenity_1 = {
            "name": "Wi-Fi"
        }
        response = self.client.post('/api/v1/amenities/', json=amenity_1)
        self.assertEqual(response.status_code, 201)

    def test_create_amenity_already_exist(self):
        amenity_2 = {
            "name": "Wi-Fi"
        }
        response = self.client.post('/api/v1/amenities/', json=amenity_2)
        self.assertEqual(response.status_code, 409)

    def test_get_all_amenities(self):
        response = self.client.get('/api/v1/amenities/', json={})
        self.assertEqual(response.status_code, 200)

    def test_get_amenity_by_id(self):
        amenity_4 = {
            "name": "Pool"
        }
        response = self.client.post('/api/v1/amenities/', json=amenity_4)
        self.assertEqual(response.status_code, 201)
        amenity4_id = response.json['id']
        response = self.client.get(f'/api/v1/amenities/{amenity4_id}', json={})
        self.assertEqual(response.status_code, 200)

    def test_get_amenity_by_bad_id(self):
        amenity_6 = {
            "name": "Haunted"
        }
        response = self.client.post('/api/v1/amenities/', json=amenity_6)
        self.assertEqual(response.status_code, 201)
        fake_id = "oh_wow"
        response = self.client.get(f'/api/v1/amenities/{fake_id}', json={})
        self.assertEqual(response.status_code, 404)

    def test_get_amenity_update(self):
        amenity_7 = {
            "name": "Roof"
        }
        response = self.client.post('/api/v1/amenities/', json=amenity_7)
        self.assertEqual(response.status_code, 201)
        amenity7_id = response.json['id']

        update_datas = {
            "name": "Windows"
        }
        response = self.client.put(f'/api/v1/amenities/{amenity7_id}',
                                   json=update_datas)
        self.assertEqual(response.status_code, 200)

    def test_get_amenity_update_wrong_id(self):
        amenity_9 = {
            "name": "Cockroaches"
        }
        response = self.client.post('/api/v1/amenities/', json=amenity_9)
        self.assertEqual(response.status_code, 201)

        update_datas = {
            "name": "Possessed chihuahua"
        }
        fake_id = "trololololo"
        response = self.client.put(f'/api/v1/amenities/{fake_id}',
                                   json=update_datas)
        self.assertEqual(response.status_code, 404)

    def test_get_amenity_update_name_already_exist(self):
        amenity_8 = {
            "name": "Expensive"
        }
        response = self.client.post('/api/v1/amenities/', json=amenity_8)
        self.assertEqual(response.status_code, 201)
        amenity_id = response.json['id']

        update_datas = {
            "name": "Wi-Fi"
        }
        response = self.client.put(f'/api/v1/amenities/{amenity_id}',
                                   json=update_datas)
        self.assertEqual(response.status_code, 409)
