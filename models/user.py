#!/usr/bin/python3
"""Define user class"""

from models.base_model import BaseModel


class User(BaseModel):
    """class User that inherits from BaseModel"""

    email: str = ""
    password: str = ""
    first_name: str = ""
    last_name: str = ""
