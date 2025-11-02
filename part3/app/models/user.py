from .base import BaseModel
from app.extensions import bcrypt, db


class User(BaseModel):
    __tablename__ = 'users'

    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), nullable=False, unique=True)
    password = db.Column(db.String(128), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)

    def add_review(self, review):
        """Add a review to the place."""
        self.reviews.append(review)

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
            "places": self.places,
            "reviews": self.reviews
            }

    def hash_password(self, password):
        """Hashes the password before storing it."""
        self.password = bcrypt.generate_password_hash(password).decode('utf-8')

    def verify_password(self, password):
        """Verifies if the provided password matches the hashed password."""
        return bcrypt.check_password_hash(self.password, password)
