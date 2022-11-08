#!/usr/bin/python3
# function that execute function safely

import sys

def safe_function(fct, *args):
    try:
        result = fct(*args)
        return (result)
    except:
        print("Exception: {}".format(sys.exc_info()[1], file=sys.stderr)
        return (None)
