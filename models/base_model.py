#!/usr/bin/python3
"""Define base_model class"""

import datetime
import uuid


class BaseModel:
    """Defines all common attributes/methods for other classes"""

    def __init__(self) -> None:
        """init new or old object"""
        self.id: str = str(uuid.uuid4())
        self.created_at: datetime = datetime.datetime.now()
        self.updated_at: datetime = datetime.datetime.now()

    def save(self) -> None:
        self.updated_at = datetime.datetime.now()

    def to_dict(self) -> dict:
        """returns a dictionary containing all keys/values of
            attributes and class name"""
        instance_dict = self.__dict__
        instance_dict["__class__"] = self.__class__.__name__
        instance_dict["created_at"] = self.created_at.isoformat()
        instance_dict["updated_at"] = self.updated_at.isoformat()

        return instance_dict

    def __str__(self) -> str:
        """string representation of class"""
        class_name = self.__class__.__name__
        return f"[{class_name}] ({self.id}) {self.__dict__}"
