#!/usr/bin/python3
"""
Initializer for uniq instance of FileStorage
"""
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.state import State
from models.place import Place
from models.review import Review
all_classes = {"Amenity": Amenity, "BaseModel": BaseModel, "City": City,
               "Place": Place, "Review": Review, "State": State} #"User": User
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
