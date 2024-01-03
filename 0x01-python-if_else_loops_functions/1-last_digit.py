#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

last_digit = 0
if number >= 0:
    last_digit = number % 10
else:
    last_digit = -10 + (number % 10)
last = "Last digit of "
neg = " and is less than 6 and not 0"
if last_digit > 5:
    print("{}{:d} is {:d} and is greater than 5".format(last, number, last_digit))
elif last_digit == 0:
    print("Last digit of {:d} is {:d} and is 0".format(number, last_digit))
else:
    print("{}{:d} is {:d}{}".format(last, number, last_digit, neg))
