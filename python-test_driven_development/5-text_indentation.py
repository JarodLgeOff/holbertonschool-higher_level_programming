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

    letters = 0
    while letters < len(text):
        print(text[letters], end="")
        if text[letters] in ['.', '?', ':']:
            print("\n")
            # Skip any spaces after the special character
            while letters + 1 < len(text) and text[letters + 1] == ' ':
                letters += 1
        letters += 1
