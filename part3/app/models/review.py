from .base import BaseModel
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey


class Review(BaseModel):
    __tablename__ = 'reviews'

    comment: Mapped[str] = mapped_column(nullable=False)
    rating: Mapped[int] = mapped_column(nullable=False)
    place_id: Mapped[str] = mapped_column(ForeignKey('places.id'), nullable=False)
    user_id: Mapped[str] = mapped_column(ForeignKey('users.id'), nullable=False)
    user = relationship('User', back_populates='reviews')
    place = relationship('Place', back_populates='reviews')


    def to_dict(self):
        return {
            "id": self.id,
            "comment": self.comment,
            "rating": self.rating,
            "user_id": self.user_id,
            "place_id": self.place_id
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
