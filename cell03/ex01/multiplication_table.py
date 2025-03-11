#!/usr/bin/python3

number = int(input("Enter a number\n"))
table = 0

while table <= 9:
    print(f"{table} x {number} = {table * number}")
    table += 1