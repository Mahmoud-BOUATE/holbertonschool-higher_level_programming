#!/usr/bin/python3
"""import le module json de python"""
import json

"""Cette foction permet de transformer en texte format JSON """


def to_json_string(my_obj):
    """Transformer my_obj en format JSON"""

    return json.dumps(my_obj)
