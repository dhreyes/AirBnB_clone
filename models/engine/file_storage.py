#!/usr/bin/python3
"""
Create of class FileStorage that cereals and decereals JSON
"""
import json
import os
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

all_classes = {"Amenity": Amenity, "BaseModel": BaseModel, "City": City,
        "Place": Place, "Review": Review, "State": State, "User": User}

class FileStorage:
    """
    Cereals and decereals JSON file to instances
    """
    __file_path = 'file.json'
    __objects = dict()

    def all(self):
        """ Returns the dictionary """
        return self.__objects

    def new(self, obj):
        """ Add object to dictionary objects """
        self.__objects[obj.__class__.__name__ + '.' + obj.id] = obj

    def save(self):
        """ cerealizes objects to JSON file, path: __file_path """
        filename = self.__file_path
        new_dic = {}
        with open(filename, mode='w', encoding='UTF-8') as myFile:
            for key, value in self.__objects.items():
                new_dic[key] = value.to_dict()
            json.dump(new_dic, myFile)

    def reload(self):
        """
        Decerealizes JSON to objects
        """
        try:
            filename = self.__file_path
            with open(filename, mode='r', encoding='UTF-8') as myFile:
                jason_file = json.load(myFile)
                """
                creates objects and searches through every class for
                the correct object class to populate key/val
                """
            for key in jason_file:
                self.__objects[key] = all_classes[jason_file[key]["__class__"]](**jason_file[key])
        except:
            pass
