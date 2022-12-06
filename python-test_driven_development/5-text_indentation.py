#!/usr/bin/python3
# function that prints a text with 2 new lines
# after each of these characters: ., ? and :
"""Define 'text_indentation' function."""


def text_indentation(text):
    """
        Print text with two new lines after each '.', '?', and ':'.
        Args:
            text (string): text to print.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    c = 0
    while c < len(text) and text[c] == ' ':
        c += 1

    while c < len(text):
        print(text[c], end="")
        if text[c] == "\n" or text[c] in ".?:":
            if text[c] in ".?:":
                print("\n")
            c += 1
            while c < len(text) and text[c] == ' ':
                c += 1
            continue
        c += 1
