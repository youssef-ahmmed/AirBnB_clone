#!/usr/bin/python3
"""Defines Amenity module"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """class Amenity that inherits from BaseModel"""

    name: str = ""
