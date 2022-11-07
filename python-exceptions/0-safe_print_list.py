#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        x >= my_list
    except KeyError:
        print(x)
