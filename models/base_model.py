#!/usr/bin/python3
"""
This module contains the BaseModel class which takes care of the initialization,
 serialization, and deserialization of instances in the AirBnB clone project.
"""
from datetime import datetime
from uuid import uuid4


class BaseModel:
    """Define all common attributes/methods for other classes."""

    def __init__(self):
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __init__(self):
        """Print: [<class name>] (<self.id>) <self.__dict__>."""

        print("[{}] ({}) {}".format(type(self).__name__, self.id, self.__dict__))

    def save(self):
        """Update updated_at attribute with the current datetime."""

        self.updated_at = datetime.now()

    def to_dict(self):
        """Return a dictionary containing all keys/values of __dict__ of the instance."""
        temp = self.__dict__
        temp['__class__'] = type(self).__name__
        temp['created_at'] = datetime.isoformat(created_at)
        temp['updated_at'] = datetime.isoformat(updated_at)
        return temp
