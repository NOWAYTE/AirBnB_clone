#!/usr/bin/python3
"""

"""

import json
import os

class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns he dictionar __object"""
        return sel.__objects

    def new(self, obj):
        """Serializes __objects the obj with key <obj class name>.id"""

        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """serializes __objects to the json file"""
        j_object = {}

        for key in self.__objects:
            j_object[key] = self.__objects[key].to_dict(dump="Yes")

        with(self.__file_path, 'w') as file:
            json.dump(self.__objects, file)
    def reload(self):
        """Deserializes the JSON file to __objects."""
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r') as file:
                obj_dict = json.load(file)
                for key, value in obj_dict.items():
                    class_name, obj_id = key.split('.')
                    class_ = globals()[class_name]
                    self.__objects[key] = class_(**value)
