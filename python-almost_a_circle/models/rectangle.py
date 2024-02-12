#!/usr/bin/python3
""" Class Rectangle """
from models.base import Base as Base


class Rectangle(Base):
    """ Rectangle Class inherits from Base class """

    def __init__(self, width, height, x=0, y=0, id=None):
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def getwidth(self, width=0):
        return self.width

    @getwidth.setter
    def setwidth(self, width):
        if width < 0:
            raise ValueError("Width can not be negative!")
        self.width = width

    @property
    def getheight(self, height=0):
        return self.height

    @getheight.setter
    def setheight(self, height):
        if height < 0:
            raise ValueError("Width can not be negative!")
        self.height = height
