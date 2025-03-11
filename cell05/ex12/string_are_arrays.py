#!/usr/bin/python3

import sys
import re

if len(sys.argv) != 2 or 'z' not in sys.argv[1]:
    print("none")
    quit()

for c in sys.argv[1]:
    if c == 'z':
        print("z", end="")
print("\n", end="")