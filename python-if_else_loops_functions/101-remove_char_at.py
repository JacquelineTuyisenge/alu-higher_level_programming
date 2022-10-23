#!/usr/bin/python3
def remove_char_at(str, n):
    position = 0
    new = ""
    for character in str:
        if position != n:
            new += character
        position += 1
    return (new)    
