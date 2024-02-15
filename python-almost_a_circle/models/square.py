#!/usr/bin/python3
"""
    Square class
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class inheriths from rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """init method"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """str method"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
