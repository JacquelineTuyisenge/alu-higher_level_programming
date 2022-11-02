#!/usr/bin/python3
def no_c(my_string):
    copy = [letter for letter in my_string if letter != 'c' and letter != 'C']
    return ("".join(copy))
