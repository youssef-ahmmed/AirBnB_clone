#!/usr/bin/python3
"""Defines Review module"""

from models.base_model import BaseModel


class Review(BaseModel):
    """Class Review that inherits from BaseModel"""

    place_id: str = ""
    user_id: str = ""
    text: str = ""
