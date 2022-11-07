#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        my_list = [1,2,3,4]
    except IndexError:
        print("Sorry that index doesn't exist")
    except:
        print("An unknown error occured")
    for n in my_list:
        return my_list[n]
