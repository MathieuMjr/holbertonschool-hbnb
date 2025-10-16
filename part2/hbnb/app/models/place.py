from .base import BaseModel
"""
This module contains a representation of Place to rent
"""


class Place(BaseModel):
    def __init__(
            self, title, description, price, latitude, longitude, owner_id):
        super().__init__()
        self.title = title
        self.description = description
        self.price = price
        self.latitude = latitude
        self.longitude = longitude
        self.owner_id = owner_id  # owner id
        self.amenities = []  # stores list of amenities
        self.reviews = []  # stores list of reviews

    def add_review(self, review):
        self.reviews.append(review)

    def add_amenity(self, amenity_id):
        self.amenities.append(amenity_id)

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "price": self.price,
            "latitude": self.latitude,
            "longitude": self.longitude,
            "owner_id": self.owner_id
        }

# # SETTERS / GETTERS

#     # TITLE
#     @property
#     def title(self):
#         return self._title

#     @title.setter
#     def title(self, value):
#         if isinstance(value, str) and len(value) <= 70 and len(value) >= 20:
#             self._title = value
#         else:
#             raise ValueError(
#                 "Title must be a string between 20 and 70 characters")

#     # Description
#     @property
#     def description(self):
#         return self._description

#     @description.setter
#     def description(self, value):
#         if isinstance(value, str)
#           and len(value) >= 150 and len(value) <= 350:
#             self._description = value
#         else:
#             raise ValueError(
#                 "Description must be a string
#                   between 150 and 350 characters")

#     # PRICE
#     @property
#     def price(self):
#         return self._price

#     @price.setter
#     def price(self, value):
#         if isinstance(value, int) and value > 0:
#             self._price = value
#         else:
#             raise ValueError("Price must be a positive integer")

#     # LATITUDE
#     @property
#     def latitude(self):
#         return self._latitude

#     @latitude.setter
#     def latitude(self, value):
#         if isinstance(value, float) and value >= -90 and value <= 90:
#             self._latitude = value
#         else:
#             raise ValueError("latitude must be a float between -90 and 90")

#     # LONGITUDE
#     @property
#     def longitude(self):
#         return self._longitude

#     @longitude.setter
#     def longitude(self, value):
#         if isinstance(value, float) and value >= -180 and value <= 180:
#             self._longitude = value
#         else:
#             raise ValueError(
#   "longitude must be a float between -180 and 180")

#     # OWNER
#     @property
#     def owner_id(self):
#         return self._owner_id

#     @owner_id.setter
#     def owner_id(self, value):
#         if isinstance(value, str) and len(value) >= 2:
#             self._owner_id = value
#         else:
#             raise ValueError(
#                 "Owner_id must be a string of 2 characters long, at least")
