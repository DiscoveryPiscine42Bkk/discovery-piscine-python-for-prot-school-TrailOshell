#!/usr/bin/python3

import sys
import re

if len(sys.argv) == 1:
    print("none")
    quit()

print(f"parameters: {len(sys.argv) - 1}")
for arg in sys.argv[1:]:
    print(f"{arg}: {len(arg)}")