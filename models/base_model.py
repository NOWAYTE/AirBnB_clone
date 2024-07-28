#!/usr/bin/python3
"""
Contains Base class Model

"""
import uuid
from datetime import datetime

time = "%Y-%m-%dT%H:%M:%S.%f"

class BaseModel:
    """BaseModel from which other classes will be derived"""

    def __init__(self, *args, **kwargs):
        """Initialize a new Base Model"""
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    if isinstance(value, str):
                        value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at

    def __str__(self):
        """Retruns a string representation of BaseModel instance"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Update the update_at attribute"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Return dictionary representation of BaseModel instance"""
        n_dict = self.__dict__.copy()
        if "created_at" in n_dict:
            n_dict['created_At'] = n_dict['created_at'].strftime(time)
        if "updated_at" in n_dict:
            n_dict['updated_at'] = n_dict['updated_at'].strftime(time)

        n_dict['__class__'] = self.__class__.__name__
        return n_dict
