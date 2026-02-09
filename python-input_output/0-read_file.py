#!/usr/bin/python3
"""ouvir un fichier en mode lecture en utilisant with"""


def read_file(filename="my_file_0.txt"):
    """Cette fonction indique le fichier à ouvrir et le mode d'ouverture"""

    with open("my_file_0.txt", 'r', encoding="utf-8") as f:
        simple_line = f.read()
    print(simple_line)
