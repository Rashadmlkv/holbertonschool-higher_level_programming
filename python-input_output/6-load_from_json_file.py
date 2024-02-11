#!/usr/bin/python3
"""
    writes object to txt file
"""
import json


def load_from_json_file(filename):
    """ returns bytes """

    with open(filename, 'w', encoding='utf-8') as f:
        return json.load(f)
