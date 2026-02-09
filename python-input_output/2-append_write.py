#!/usr/bin/python3
"""ouvir un fichier en mode append en utilisant with"""


def append_write(filename="", text=""):
    """Cette fonction indique le fichier ou va rajouter txt et le mode ouver"""

    with open(filename, 'a', encoding="utf-8") as f:
        f.write(text)
        return len(text)
