#!/usr/bin/python3
"""
    writes object to txt file
"""
import json


def save_to_json_file(my_obj, filename):
    """ returns bytes """

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(str(json.dumps(my_obj)))
