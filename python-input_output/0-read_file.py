#!/usr/bin/python3

"""0. Read a file"""


def read_file(filename=""):
    with open(filename, encoding="utf-8") as f:
        print(f.read())
        f.close()
