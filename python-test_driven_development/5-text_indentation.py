#!/usr/bin/python3

"""
This module defines a function that prints a text with
2 new lines after each '.', '?', and ':' character.
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each '.', '?', and ':' character.
    Args:
        text (str): The text to be indented.
    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    new_text = text.replace('. ', '.\n\n')
    new_text1 = new_text.replace('? ', '?\n\n')
    new_text2 = new_text1.replace(': ', ':\n\n')

    print(new_text2, end="")
