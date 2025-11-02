from abc import ABC, abstractmethod
from app.extensions import db


class Repository(ABC):
    @abstractmethod
    def add(self, obj):
        pass

    @abstractmethod
    def get(self, obj_id):
        pass

    @abstractmethod
    def get_all(self):
        pass

    @abstractmethod
    def update(self, obj_id, data):
        pass

    @abstractmethod
    def delete(self, obj_id):
        pass

    @abstractmethod
    def get_by_attribute(self, attr_name, attr_value):
        pass

class SQLAlchemyRepository(Repository):
    def __init__(self, model):
        self.model = model

    def add(self, obj):
        db.session.add(obj)
        db.session.commit()

    def get(self, obj_id):
        return self.model.query.get(obj_id)

    def get_all(self):
        return self.model.query.all()

    def update(self, obj_id, data):
        obj = self.get(obj_id)
        if obj:
            obj.update
            if 'password' in data:
                obj.hash_password(obj.password)
            db.session.commit()

    def delete(self, obj_id):
        obj = self.get(obj_id)
        if obj:
            db.session.delete(obj)
            db.session.commit()

    def get_by_attribute(self, attr_name, attr_value):
        return self.model.query.filter_by(**{attr_name: attr_value}).first()


class InMemoryRepository(Repository):
    def __init__(self):
        """
        This function save an object into a dict
        """
        self._storage = {}

    def add(self, obj):
        """
        This function retrieve an object
        by its id
        """
        self._storage[obj.id] = obj

    def get(self, obj_id):
        """
        This function retrieve an object
        by its id
        """
        return self._storage.get(obj_id)

    def get_all(self):
        """
        This function retrieve all object
        of a kind that are know
        """
        return list(self._storage.values())

    def update(self, obj_id, data):
        """
        This function udpate an object
        if its id exist
        """
        obj = self.get(obj_id)
        if obj:
            obj.update(data)  # use update method from base class in models
            if 'password' in data:
                obj.hash_password(obj.password)

    def delete(self, obj_id):
        """
        This method delete an object
        """
        if obj_id in self._storage:
            del self._storage[obj_id]

    def get_by_attribute(self, attr_name, attr_value):
        """
        This function retrieve an object
        through an attribute
        """
        return next(
            (obj for obj in self._storage.values() if getattr(obj, attr_name) == attr_value), None)
