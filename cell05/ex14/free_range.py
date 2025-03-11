#!/usr/bin/python3

import sys

try:
    if len(sys.argv) != 3:
        print("none")
        quit()

    if sys.argv[1] >= sys.argv[2]:
        array = list(range(int(sys.argv[1]), int(sys.argv[2]) + 1))
    elif sys.argv[1] < sys.argv[2]:
        array = list(reversed(range(int(sys.argv[2]), int(sys.argv[1]) + 1)))
    print(array)

except:
    print("Error")