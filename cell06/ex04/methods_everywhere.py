#!/usr/bin/python3

import sys

def shrink(string):
    return string[:8]

def enlarge(string):
    return string + 'Z' * (8 - len(string))

if len(sys.argv) == 1:
    print("none")
    quit()

for arg in sys.argv[1:]:
    length = len(arg)
    if length > 8:
        print(shrink(arg))
    elif length < 8:
        print(enlarge(arg))
    elif length == 8:
        print(arg)