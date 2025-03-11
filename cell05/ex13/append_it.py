#!/usr/bin/python3

import sys

if len(sys.argv) == 1:
    print("none")
    quit()

for arg in sys.argv[1:]:
    if arg.endswith("ism"):
        continue
    else:
        print(x + "ism")