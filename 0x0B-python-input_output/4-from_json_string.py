#!/usr/bin/python3
"""JSON to object"""
import json


def from_json_string(my_str):
    """Converts JSON to object"""

    return json.loads(my_str)
