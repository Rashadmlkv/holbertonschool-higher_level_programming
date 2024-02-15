#!/usr/bin/python3i
""" Class Rectangle """
from models.base import Base as Base


class Rectangle(Base):
    """ Rectangle Class inherits from Base class """

    def __init__(self, width, height, x=0, y=0, id=None):
        """initialize"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """ area """
        return self.width * self.height

    def display(self):
        """display with #"""
        if self.y != 0:
            for _ in range(self.y):
                print()
        for i in range(self.height):
            for _ in range(self.x):
                print(" ", end="")
            print("#" * self.width)

    def __str__(self):
        """ print """
        return f"[Rectangle] ({self.id}) \
{self.x}/{self.y} - {self.width}/{self.height}"

    def update(self, *args, **kwargs):
        """ learning *args """
        if (len(args) != 0):
            counter = 0
            atrs = ['id', 'width', 'height', 'x', 'y']
            for arg in args:
                setattr(self, atrs[counter], arg)
                counter += 1
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """return fielsds  dict"""
        tmpdct = {'x': self.x, 'y': self.y, 'id': self.id,\
'height': self.height, 'width': self.width}
        return tmpdct
