from .base import BaseModel


class Review(BaseModel):
    def __init__(self, comment, rating, place_id, author_id):
        super().__init__()
        self.comment = comment
        self.rating = rating
        self.place_id = place_id
        self.author_id = author_id

    def to_dict(self):
        return {
            "comment": self.comment,
            "rating": self.rating,
            "place_id": self.place_id,
            "owner_id": self.author_id
        }

# # SETTER/GETTER
# #   COMMENT
#     @property
#     def comment(self):
#         return self._comment

#     @comment.setter
#     def comment(self, value):
#         if isinstance(value, str) and len(value) <=350 and len(value) >= 30:
#             self._comment = value
#         else:
#             raise ValueError(
# "Comment must be a string between 30 and 350 characters")

# #   RATING
#     @property
#     def rating(self):
#         return self._rating

#     @rating.setter
#     def rating(self, value):
#         if isinstance(value, int) and value >= 0 and value <= 5:
#             self._rating = value
#         else:
#             raise ValueError("Rating must be an integer between 0 and 5")

# #   PLACE_ID
#     @property
#     def place_id(self):
#         return self._owner

#     @place_id.setter
