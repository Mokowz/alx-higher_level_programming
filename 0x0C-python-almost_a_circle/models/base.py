#!/usr/bin/python3
"""
Define a bass class
"""


class Base:
    """Define the base class
    Attributes:
        id: Identity
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Instantiate the base class
        Args:
            id: Identity
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
