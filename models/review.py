#!/usr/bin/env python3
"""Review class module"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Review class instance"""
    place_id = ""
    user_id = ""
    text = ""
