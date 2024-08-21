#!/usr/bin/python3
"""Defines a base model"""

import uuid
from datetime import datetime 

class BaseModel:
    """Base class Model """
    def __init__(self):
        """Initialization"""
        self.id = uuid.uuid4()
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    def __str__(self):
        """Print format"""
        return "[{}] ({}) {}".format(BaseModel.__name__, self.id, self.__dict__)

    def save(self):
        """Update the updated_at public instance attr"""
        updated_at = datetime.now()

    def to_dict(self):
        """Return a dictionary"""
        obj_dict =  self.__dict__.copy()
        obj_dict["__class__"] = BaseModel.__name__
        obj_dict["created_at"] = self.created_at.isoformat()
        obj_dict["updated_at"] = self.updated_at.isoformat()


        return obj_dict
