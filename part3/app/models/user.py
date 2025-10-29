from .base import BaseModel
from app.extensions import bcrypt


class User(BaseModel):
    def __init__(self, last_name, first_name, email, password, is_admin=False):
        super().__init__()
        self.last_name = last_name
        self.first_name = first_name
        self.email = email
        self.is_admin = is_admin
        self.password = password
        self.places = []  # List to store related places

    def add_place(self, place_id):
        self.places.append(place_id)

    def to_dict(self):
        """
        This function allow to display some specific attribute of user.
        Usefull to avoid to return passwords, for example (will be implemented
        later)"""
        return {
            "id": self.id,
            "last_name": self.last_name,
            "first_name": self.first_name,
            "email": self.email,
            "is_admin": self.is_admin,
            "places": self.places
            }

    def hash_password(self, password):
        """Hashes the password before storing it."""
        self.password = bcrypt.generate_password_hash(password).decode('utf-8')

    def verify_password(self, password):
        """Verifies if the provided password matches the hashed password."""
        return bcrypt.check_password_hash(self.password, password)
