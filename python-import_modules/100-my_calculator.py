#!/usr/bin/python3
from sys import argv
from calculator_1 import add, sub, mul, div

if __name__ == "__main__":
    number = len(argv)

    if number != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    a = int(argv[1])
    c = argv[2]
    b = int(argv[3])

    if c == "+":
        num = add(a, b)
    elif c == "-":
        num = sub(a, b)
    elif c == "/":
        num = div(a, b)
    elif c == "*":
        num = mul(a, b)
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    print("{:d} {} {:d} = {:d}".format(a, c, b, num))
