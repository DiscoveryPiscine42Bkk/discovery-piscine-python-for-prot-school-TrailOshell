#!/usr/bin/python3

def greetings(string = "noble stranger"):
    if isinstance(string, str):
        print("Hello, " + string + ".")
    else:
        print("Error! It was not a name.")

greetings('Alexandra')
greetings('Wil')
greetings()
greetings(42)