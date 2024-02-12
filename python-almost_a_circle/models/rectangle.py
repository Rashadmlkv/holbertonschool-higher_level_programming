#!/usr/bin/python3
""" Class Rectangle """
from models.base import Base as Base


class Rectangle(Base):
    """ Rectangle Class inherits from Base class """

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self, width=0):
        return self.__width

    @width.setter
    def width(self, width):
        self.__width = width

    @property
    def height(self, height=0):
        return self.__height

    @height.setter
    def height(self, height):
        self.__height = height
