#!/usr/bin/python3
"""import le module json de python"""
import json

"""Cette foction permet de transformer txt en format JSON """


def from_json_string(my_str):
    """Transformer my_str en format objet"""

    return json.loads(my_str)
