#!/usr/bin/python3

import sys
import re

if len(sys.argv) != 3 or sys.argv[1] not in sys.argv[2]:
    print("none")
    quit()

count = len(re.findall(sys.argv[1], sys.argv[2]))
print(count)