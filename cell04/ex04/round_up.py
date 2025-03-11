#!/usr/bin/python3

try:
    number = float(input("Give me a number: "))
    round_up = int(number) + (number % 1 > 0)
    print(round_up)
except:
    print("Error") 