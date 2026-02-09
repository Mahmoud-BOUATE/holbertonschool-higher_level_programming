#!/usr/bin/python3
"""ouvir un fichier en mode lecture en utilisant with"""

def write_file(filename="my_file_0.txt", text="This School is so cool!\n"):
    """Cette fonction indique le fichier ou va écrir et le mode d'ouverture"""

    with open(filename, 'w', encoding="utf-8") as f:
        return len(text)
