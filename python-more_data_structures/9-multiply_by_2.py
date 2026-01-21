#!/usr/bin/python3


def multiply_by_2(a_dictionary):
    copy_dictionary = a_dictionary.copy()

    for key in copy_dictionary:
        copy_dictionary[key] = copy_dictionary[key] * 2

    return copy_dictionary
