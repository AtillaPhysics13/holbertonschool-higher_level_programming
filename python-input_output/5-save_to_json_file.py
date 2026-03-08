#!/usr/bin/python3
"""Module change strind and write file"""

import json


def save_to_json_file(my_obj, filename):
    """Returns the change of the string and write file"""
    with open(filename, "w") as f:
        json.dump(my_obj, f)
