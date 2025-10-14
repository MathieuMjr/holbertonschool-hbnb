from .base import BaseModel


class User(BaseModel):
    def __init__(self, last_name, first_name, email, is_admin=False):
        super().__init__()
        self.last_name = last_name
        self.first_name = first_name
        self.email = email
        self.is_admin = is_admin
        self.places = []  # List to store related places²
