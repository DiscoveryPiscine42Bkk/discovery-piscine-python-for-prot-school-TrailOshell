#!/usr/bin/python3

number = int(input("Enter a number less than 25\n"))
if number > 25:
    print("Error")
elif number <= 25:
    while number <= 25:
        print(f"Inside the llop, my variable is {number}")
        number += 1