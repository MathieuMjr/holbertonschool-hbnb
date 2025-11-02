from .base import BaseModel
from sqlalchemy.orm import Mapped, mapped_column


class Amenity(BaseModel):
    __tablename__ = 'amenities'

    name: Mapped[str] = mapped_column(nullable=False, unique=True)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name
        }
