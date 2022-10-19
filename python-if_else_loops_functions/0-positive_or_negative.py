#!/usr/bin/python3
import random
number = random.randint(-10, 10)
def pnive(x):
if x > 0:
    print(f"{x} is positive\n")
elif x == 0:
    print(f"{x} is zero\n")
else: x < 0:
    print(f"{x} is negative\n")
pnive(number)
