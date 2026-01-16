#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":

    if len(argv) < 2:
        print("0")
    else:
        total = 0

        for arg in argv[1:]:
            total += int(arg)
        print(total)
