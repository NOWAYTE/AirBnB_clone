#!/usr/bin/python3

import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

class FileStorage:
    """Serializes instances to a JSON file and deserializes JSON file to instances."""

    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """Returns the dictionary __objects."""
        return self.__objects

    def new(self, obj):
        """Adds a new object to the __objects dictionary."""
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """Saves the __objects dictionary to a JSON file."""
        with open(self.__file_path, 'w') as f:
            json.dump(self.all_dict(), f)

    def all_dict(self):
        """Returns the dictionary representation of __objects."""
        return {k: v.to_dict() for k, v in self.__objects.items()}

    def reload(self):
        """Loads the JSON file and creates instances based on the data."""
        try:
            with open(self.__file_path, 'r') as f:
                objs = json.load(f)
            for key, val in objs.items():
                class_name = val['__class__']
                self.new(eval(class_name)(**val))  # Create an instance using ** unpacking
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """Deletes an object from the __objects dictionary."""
        if obj:
            key = f"{obj.__class__.__name__}.{obj.id}"
            if key in self.__objects:
                del self.__objects[key]

