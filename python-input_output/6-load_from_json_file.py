#!/usr/bin/python3
"""Module change strind and write file"""

import json


def load_from_json_file(filename):
    """Returns the change of the string and write file"""
    with open(filename, "r") as f:
        return json.load(f)
