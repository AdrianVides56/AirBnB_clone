#!/usr/bin/python3
""" Intializing module """
import uuid
from datetime import datetime


class BaseModel:
    """ base class """
    def __init__(self):
        """ Initial state of an object """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """ String representation of object """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id,
                                     self.__dict__)

    def save(self):
        """ Saves """
        self.updated_t = datetime.now()

    def to_dict(self):
        """ Returns a dictionary containing key/values of an instance """
        return self.__dict__
