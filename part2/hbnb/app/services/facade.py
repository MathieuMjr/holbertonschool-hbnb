from app.persistence.repository import InMemoryRepository
from app.models.user import User
from app.models.amenity import Amenity


class HBnBFacade:
    def __init__(self):
        self.user_repo = InMemoryRepository()
        self.place_repo = InMemoryRepository()
        self.review_repo = InMemoryRepository()
        self.amenity_repo = InMemoryRepository()

# --- USER CRUD ----------------------------------
    def create_user(self, user_data):
        """
        This function create a new
        And save it in the repo
        """
        user = User(**user_data)  # method from class User in models
        self.user_repo.add(user)  # method from repository class in persistence
        return user

    def get_user(self, user_id):
        """
        This function retrieve a user
        by its id
        """
        return self.user_repo.get(user_id)  # method from repo

    def get_user_by_email(self, email):
        """
        This function retrieve a user
        by its email
        """
        return self.user_repo.get_by_attribute('email', email)
    # method from repo

    def get_all(self):
        """
        This function retrieve all users
        known in a list
        """
        return self.user_repo.get_all()  # method from repo

    def update(self, obj_id, data):
        """
        This function modify a user
        """
        return self.user_repo.update(obj_id, data)
    # method from repo

# --- AMENITY CRUD ----------------------------------

    def create_amenity(self, amenity_data):
        amenity = Amenity(**amenity_data)
        self.amenity_repo.add(amenity)
        return amenity

    def get_amenity(self, amenity_id):
        return self.amenity_repo.get(amenity_id)

    def get_all_amenities(self):
        return self.amenity_repo.get_all()

    def update_amenity(self, amenity_id, amenity_data):
        return self.amenity_repo.update(amenity_id, amenity_data)

    def get_by_attribute(self, attr_name, attr_value):
        return self.amenity_repo.get_by_attribute(attr_name, attr_value)

# --- PLACE CRUD ------------------------------------

    def get_place(self, place_id):
        # Logic will be implemented in later tasks
        pass
