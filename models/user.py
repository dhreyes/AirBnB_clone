#!/usr/bin/python3
""" User class module """
from models.base_model import BaseModel


class User(BaseModel):
    """ Empty User class for user data """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
