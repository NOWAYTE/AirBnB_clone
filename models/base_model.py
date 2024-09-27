#!/usr/bin/python3

from uuid import uuid4
from datetime import datetime

class BaseModel:
    def __init__(self, *args, **kwargs):
        """Initialization method for BaseModel."""
        if kwargs:
            # Initialize object from deserialized data
            for key, value in kwargs.items():
                if key not in ('__class__', 'created_at', 'updated_at'):
                    setattr(self, key, value)
            self.created_at = datetime.strptime(kwargs['created_at'], "%Y-%m-%dT%H:%M:%S.%f")
            self.updated_at = datetime.strptime(kwargs['updated_at'], "%Y-%m-%dT%H:%M:%S.%f")
        else:
            # Create a new instance
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

            # Avoid circular import by doing this import locally
            from models import storage
            storage.new(self)

    def save(self):
        """Updates updated_at and saves instance to storage."""
        self.updated_at = datetime.now()

        # Avoid circular import by importing storage locally
        from models import storage
        storage.save()

    def to_dict(self):
        """Returns dictionary representation of an instance."""
        dictionary = self.__dict__.copy()
        dictionary["__class__"] = self.__class__.__name__
        dictionary["created_at"] = self.created_at.isoformat()
        dictionary["updated_at"] = self.updated_at.isoformat()
        return dictionary

