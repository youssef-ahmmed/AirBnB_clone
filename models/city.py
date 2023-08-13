#!/usr/bin/python3
"""Define city class"""

from models.base_model import BaseModel


class City(BaseModel):
    """class City that inherits from BaseModel"""

    state_id: str = ""
    name: str = ""

    def __init__(self, *args, **kwargs):
        """init the City object"""
        super().__init__(*args, **kwargs)
