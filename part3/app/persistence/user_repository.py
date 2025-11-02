from app.models.user import User
from app.extensions import db
from app.persistence.repository import SQLAlchemyRepository


class UserRepository(SQLAlchemyRepository):
    def __init__(self):
        super().__init__(User)
        # tell SQL alchemy to use User model
        # check in repository.py > class SQLAlchemyrepository
        # > init takes a model as parameter

    def get_user_by_email(self, email):
        return self.model.query.filter_by(email=email).first()
        # specific request for get a user by email
        # this one can't be defined in SQLAlchemmyrepository class
        # cause it would create it for all the others repos. 