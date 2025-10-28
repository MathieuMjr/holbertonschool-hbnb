import uuid
from datetime import datetime
"""
This module contains the basemodel class for
models objetcs.
"""


class BaseModel:
    def __init__(self):
        """
        Objects attributes :
        - id : unique ID generated via uuid module
        - creation date
        - update date : modified each time the object is modified
        """
        self.id = str(uuid.uuid4()) # str typecast necessary so it is serialisable in json
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def save(self):
        """Update the updated_at timestamp whenever the object is modified"""
        self.updated_at = datetime.now()

    def update(self, data): # data is a dict with key and value to modify
        """Update the attributes of the object based on the provided dictionary"""
        for key, value in data.items():
            if hasattr(self, key): # is key in data in self ?
                setattr(self, key, value)
        self.save()  # Update the updated_at timestamp
