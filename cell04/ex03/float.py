#!/usr/bin/python3

try:
    number = float(input("Give me a number: "))

    if number.is_integer() == 1:
        print("This number is an integer")
    elif number.is_integer() == 0:
        print("This number is a decimal")
except:
    print("Error") 