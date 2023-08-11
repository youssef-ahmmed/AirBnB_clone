#!/usr/bin/python3
"""Define city class"""

from models.base_model import BaseModel


class City(BaseModel):
    """class City that inherits from BaseModel"""

    state_id: str = ""
    name: str = ""
