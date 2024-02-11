#!/usr/bin/python3
"""
    inherit directly or not
"""


def inherits_from(obj, a_class):
    """
        true false
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
