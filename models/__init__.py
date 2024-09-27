#!/usr/bin/python3

from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.state import State  # Import the State class
from models.city import City  # Import the City class
from models.amenity import Amenity  # Import the Amenity class
from models.place import Place  # Import the Place class
from models.review import Review  # Import the Review class

storage = FileStorage()
storage.reload()

# Add to the classes dictionary
classes = {
    'BaseModel': BaseModel,
    'User': User,
    'State': State,  # Add State class
    'City': City,  # Add City class
    'Amenity': Amenity,  # Add Amenity class
    'Place': Place,  # Add Place class
    'Review': Review,  # Add Review class
}

