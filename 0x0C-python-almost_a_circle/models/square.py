#!/usr/bin/python3
"""Defines a square class"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Sqaure class"""
    def __init__(self, size, x=0, y=0, id=None):
        """Initialize the sqaure class
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Repr of square"""
        return ("[Square] ({}) {:d}/{:d} - {:d}".
                format(self.id, self.x, self.y, self.size))

    @property
    def size(self):
        """size getter
        Returns:
            int: size
        """
        return self.width

    @size.setter(self, value):
        """size setter

        Args:
            value: width
        Raises:
            TypeError: widht must be integer
            ValueError: width must be > 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        
        self.width = value
        self.height = value
