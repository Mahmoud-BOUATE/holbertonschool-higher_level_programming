#!/usr/bin/python3
"""Module return true  if the object is an instance of
 a class that inherited (directly or indirectly) from the specified class """


def inherits_from(obj, a_class):
    """Retourne True si obj est exactement une instance de sous a_class,"""
    if issubclass(obj, a_class):
        return True
    else:
        return False
