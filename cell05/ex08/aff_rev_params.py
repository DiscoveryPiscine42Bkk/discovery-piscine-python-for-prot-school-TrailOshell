#!/usr/bin/python3

import sys

if len(sys.argv) < 2:
    print("none")
    quit()

for arg in reversed(sys.argv[1:]):
    print (arg)