#!/usr/bin/python3

import sys
import re

if len(sys.argv) != 2:
    print("none")
    quit()

answer = input("What was the parameter? ")

if answer == sys.argv[1]:
    print("Good job!")
else:
    print("Nope, sorry...")