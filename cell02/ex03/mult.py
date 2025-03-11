#!/usr/bin/python3

first_nb = int(input("Enter the first number:\n"))
second_nb = int(input("Enter the second number:\n"))

result = first_nb * second_nb

print(f"{first_nb} x {second_nb} = {result}")
if result > 0:
    print("The result is positive.")
elif result < 0:
    print("The result is negative.")
else:
    print("The result is both positive and negative.")