#!/usr/bin/python3

try:
    first_nb = int(input("Give me the first number: "))
    second_nb = int(input("Give me the second number: "))
    print("Thank you!")
    print(f"{first_nb} + {second_nb} = {first_nb + second_nb}")
    print(f"{first_nb} - {second_nb} = {first_nb - second_nb}")
    print(f"{first_nb} / {second_nb} = {first_nb / second_nb}")
    print(f"{first_nb} * {second_nb} = {first_nb * second_nb}")
    print(first_nb / second_nb)
except:
    print("Error") 