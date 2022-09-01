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
        self.updated_at = None

    def save(self):
        """Update updated_at attribute with the current datetime."""

        self.updated_at = datetime.now()
