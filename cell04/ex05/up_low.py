#!/usr/bin/python3

try:
    input = input()
    length = len(input)
    i = 0
    while i < length:
        if (input[i].islower()):
            print(input[i].upper(), end='')
        elif (input[i].isupper()):
            print(input[i].lower(), end='')
        else:
            print(input[i], end='')
        i += 1
    print("\n", end='')
except:
    print("Error") 