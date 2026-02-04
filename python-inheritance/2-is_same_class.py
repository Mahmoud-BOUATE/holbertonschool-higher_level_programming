#!/usr/bin/python3
"""Module return true if the objet is exactly an instance"""


def is_same_class(obj, a_class):
    """Retourne True si obj est exactement une instance de a_class,or False."""
    if type(obj) is a_class:
        return True
    else:
        return False
