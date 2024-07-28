#!/usr/bin/python3
"""
Contains Base class Model

"""

import uuid
from datetime import datetime

time = "%Y-%m-%dT%H:%M:%S.%f"

class BaseModel:
    def __init__(self, *args, **kwargs):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at


        self.name = kwargs.get("name", '')
        self.my_number = kwargs.get("my_number", '')

    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        n_dict = self.__dict__.copy()
        if "created_at" in n_dict:
            n_dict['created_At'] = n_dict['created_at'].strftime(time)
        if "updated_at" in n_dict:
            n_dict['updated_at'] = n_dict['updated_at'].strftime(time)

        n_dict['__class__'] = self.__class__.__name__


        return n_dict

