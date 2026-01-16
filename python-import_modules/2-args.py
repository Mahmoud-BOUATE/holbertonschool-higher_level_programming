#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    nb = len(argv) - 1
    if nb > 0:
        if nb == 1:
            print(f"{nb} argument:")
        else:
            print(f"{nb} arguments:")
        for i in range(1, len(argv)):
            print(f"{i}: {argv[i]}")
    else:
        print("0 arguments.")
