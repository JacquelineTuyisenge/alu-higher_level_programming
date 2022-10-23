#!/usr/bin/python3
from calculator_1 import maths
if __name__ == "__main__":
    a = 10
    b = 5
    add = a + b
        return (add)
    sub = a - b
        return (sub)
    mul = a * b
        return (mul)
    div = a / b
        return (div)
    print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
    print("{:d} - {:d} = {:d}".format(a, b, sub(a, b)))
    print("{:d} * {:d} = {:d}".format(a, b, mul(a, b)))
    print("{:d} / {:d} = {:d}".format(a, b, div(a, b)))
