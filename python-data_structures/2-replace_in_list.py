#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    for idx in my_list:
        if idx < 0 or idx > (len(my_list)):
            return no modification
        else:
            return my_list[idx(element)]
