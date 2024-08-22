#!/usr/bin/python3
"""Represents the File storage class"""

import json
import os
from models.base_model import BaseModel


class FileStorage:
    """FileStorage class"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary"""

        return self.__objects

    def new(self, obj):
        """Sets obj key """
        key = f"{obj.__class__.__name__}.{obj.id}"

        self.__objects[key] = obj

    def save(self):
        """Serializes the JSON to file"""
        json_objects = {}

        for key in self.__objects:
            json_objects[key] =  obj.to_dict()

        with open(self.__file_path, "w") as file:
            json.dump(json_objects, file, indent=4)


    def reload(self):
        """Deserializes JSON file """
        if os.path.exists(self.__file_path):
            try:
                with open(self.__file_path, "r") as file:
                    obj_dict = json.loads(file)

                    for key, value in obj_dict.items():
                        class_name, obj_id =  key.split(".")
                        cls = globals()[class_name]
                        self.__objects[key] = cls(**values)

            except:
                pass
