#!/usr/bin/python3
import random
number = random.randint(-10, 10)

def pnive(x):

    if x > 0:
       print(f"{x} is positive")
    elif x < 0:
         print(f"{x} is negative")
    else:
        print(f"{x} is negative")

pnive(number)
