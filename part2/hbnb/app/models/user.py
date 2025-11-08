from .base import BaseModel


class User(BaseModel):
    def __init__(self, last_name, first_name, email, password, is_admin=False):
        super().__init__()
        self.last_name = last_name
        self.first_name = first_name
        self.email = email
        self.is_admin = is_admin
        self.password = password
        self.places = []  # List to store related places

    # method to add a place

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
            "is_admin": self.is_admin
            }
