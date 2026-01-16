#!/usr/bin/python3
from sys import argv

if len(argv) > 1:
    print(f"{len(argv) - 1} arguments:")
    for i in range(1, len(argv)):
        print(f"{i}: {argv[i]}")
else:
    print("0 arguments.")
