#!/usr/bin/python3
"""Define base_model class"""

import datetime
import uuid
import models


class BaseModel:
    """Defines all common attributes/methods for other classes"""

    def __init__(self, *args, **kwargs) -> None:
        """init new or old object"""
        if not kwargs:
            self.id: str = str(uuid.uuid4())
            self.created_at: datetime = datetime.datetime.now()
            self.updated_at: datetime = datetime.datetime.now()
            models.storage.new(self)
            return

        self._create_instance_from_dict(*args, **kwargs)

    def _create_instance_from_dict(self, *_args, **kwargs) -> None:
        """create new instance from dictionary input"""
        for k, value in kwargs.items():
            if k in ["updated_at", "created_at"]:
                time_format: str = "%Y-%m-%dT%H:%M:%S.%f"
                time: datetime = datetime.datetime.strptime(value, time_format)
                setattr(self, k, time)
                continue
            if k != "__class__":
                setattr(self, k, value)

    def save(self) -> None:
        """Updates the updated_at and calls storage save method"""
        self.updated_at = datetime.datetime.now()
        models.storage.save()

    def to_dict(self) -> dict:
        """returns a dictionary containing all keys/values of
            attributes and class name"""
        instance_dict = self.__dict__.copy()
        instance_dict["__class__"] = self.__class__.__name__
        instance_dict["created_at"] = self.created_at.isoformat()
        instance_dict["updated_at"] = self.updated_at.isoformat()

        return instance_dict

    def __str__(self) -> str:
        """string representation of class"""
        class_name = self.__class__.__name__
        return f"[{class_name}] ({self.id}) {self.__dict__}"
