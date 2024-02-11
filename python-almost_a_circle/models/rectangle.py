#!/usr/bin/python3
""" Class Rectangle """
from models.base import Base as Base


class Rectangle(Base):
    """ Rectangle Class inherits from Base class """

    width = 0
    height = 0
    x = 0
    y = 0

    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def getwidth(self, width=0):
        return self.__width

    @getwidth.setter
    def setwidth(self, width):
        if width < 0:
            raise ValueError("Width can not be negative!")
        self.__width = width

    @property
    def getheight(self, height=0):
        return self.__height

    @getheight.setter
    def setheight(self, height):
        if height < 0:
            raise ValueError("Width can not be negative!")
        self.__height = height
