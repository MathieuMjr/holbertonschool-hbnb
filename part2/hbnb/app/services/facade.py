from app.persistence.repository import InMemoryRepository
from app.models.user import User
from app.models.amenity import Amenity
from app.models.place import Place


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

    def create_place(self, place_data):
        # VALUES VALIDATIONS:
        if place_data["price"] <= 0:
            raise ValueError(
                "Invalid input data: price must be a positive float")
        if not -90 <= place_data["latitude"] <= 90:
            raise ValueError(
                "Invalid input data: latitude value must be between -90 and 90"
                )
        if not -180 <= place_data["longitude"] <= 180:
            raise ValueError(
                "Invalid input data: longitude value must be between "
                "-180 and 180"
            )
        # OWNER ID CHECK:
        owner_id = place_data.get("owner_id")
        if owner_id:
            if not self.user_repo.get(owner_id):
                raise LookupError(f"Owner id not found: {owner_id}")
        # AMENITY EXTRACT:
        amenities_ids = place_data.pop("amenities", None)
        # PLACE CREATION:
        place = Place(**place_data)
        # AMENITY LIST MANAGEMENT
        if amenities_ids:
            for element in amenities_ids:
                if self.amenity_repo.get(element):
                    place.add_amenity(element)
                else:
                    # CHECK AMENITY ID
                    raise LookupError(f"Amenity id not found:{element}")
        self.place_repo.add(place)
        return place

    def get_place(self, place_id):
        return self.place_repo.get(place_id)

    def get_all_places(self):
        return self.place_repo.get_all()

    def update_place(self, place_id, place_data):
        if "price" in place_data:
            if place_data["price"] <= 0:
                raise ValueError(
                    "Invalid input data: price must be a positive float")
        if "latitude" in place_data:
            if not -90 <= place_data["latitude"] <= 90:
                raise ValueError(
                    "Invalid input data: latitude value must be "
                    "between -90 and 90"
                    )
        if "longitude" in place_data:
            if not -180 <= place_data["longitude"] <= 180:
                raise ValueError(
                    "Invalid input data: longitude value must be between "
                    "-180 and 180"
                )
        return self.place_repo.update(place_id, place_data)
