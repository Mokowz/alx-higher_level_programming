#!/usr/bin/python3
"""Defines rectangle class"""


from models.base import Base


class Rectangle(Base):
    """Defines the rectangle class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize the rectangle class"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Width getter
        Returns:
            int: width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Width setter

        Args:
            value: Width value

        Raises:
            TypeError: raise if width is not int
            ValueError: raise if width is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Heihgt getter
        Returns:
            int: height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Height setter

        Args:
            value: height

        Raises:
            TypeError: height is not an int
            ValueError: height is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("heihgt must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """x getter
        Returns:
            int: x
        """
        return self.__x

    @x.setter
    def x(self, value):
        """x setter

        Args:
            value: x

        Raises:
            TypeError: x must be integer
            ValueError: x must be more thna 0
        """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """y getter
        Returns:
            int: y
        """
        return self.__y

    @y.setter
    def y(self, value):
        """y setter

        Args:
            value: y

        Raises:
            TypeError: y must be int
            ValueError: y must be positive
        """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Finds the area
        Returns:
            int: area
        """
        return self.__width * self.__height

    def display(self):
        """Display the rectangle
        """
        for i in range(self.__height):
            for j in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """String repr of the rectangle"""
        return f"[Rectangle] ({self.id}) {self.__x}/{self.__y} - {self.__width}/{self.__height}"
