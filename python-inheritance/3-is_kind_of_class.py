#!/usr/bin/python3
"""Module return true  if the object is an instance of a,
class that inherited from, the specified class"""


def is_kind_of_class(obj, a_class):
    """Retourne True si obj est exactement une instance de a_class,or False."""
    if isinstance(obj, a_class):
        return True
    else:
        return False
