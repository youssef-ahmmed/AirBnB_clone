#!/usr/bin/python3
"""Define state class"""

from models.base_model import BaseModel


class State(BaseModel):
    """class State that inherits from BaseModel"""

    name: str = ""
