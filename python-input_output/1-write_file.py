#!/usr/bin/python3
"""ouvir un fichier en mode lecture en utilisant with"""


def write_file(filename="", text=""):
    """Cette fonction indique le fichier ou va écrir et le mode d'ouverture"""

    with open(filename, 'w', encoding="utf-8") as f:
        f.write(text)
        return len(text)
