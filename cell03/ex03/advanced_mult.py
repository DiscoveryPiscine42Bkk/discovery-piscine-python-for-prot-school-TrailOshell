#!/usr/bin/python3

import sys

if sys.argv[1:]:
    print("none")
    quit()

table = 0
while table <= 10:
    print(f"Table de {table}: ", end='')
    number = 0
    while number <= 10:
        print(f"{table * number}", end='')
        number += 1
        if number <= 10:
            print(" ", end='')
    print("\n", end='')
    table += 1