#!/usr/bin/python3

def max_integer(my_list=[]):

    max_value = my_list[0]

    if len(my_list) == 0:
        return None

    for value in my_list:
        if value > max_value:
            max_value = value

    return max_value
