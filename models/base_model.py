#!/usr/bin/python3
"""Basemodel that defines all common attributes/methods for other classes """
import uuid
import datetime
class BaseModel:
    """Base model class"""
    def __init__(self):
        """Initialize"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = self.created_at

    def __str__(self):
        """Return a string representation"""
        return f"[{self.__class__.__name__}] + ({self.id}) + {self.__dict__}"
    
    def save(self):
        """updates the public instance attribute updated_at with the current datetime"""
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """returns a dict representation of the instance"""
        self.created_at = self.created_at.isoformat()
        self.updated_at = self.updated_at.isoformat()
        new_dict = {**self.__dict__, **{"__class__": self.__class__.__name__}}
        return new_dict


