#!/usr/bin/env python3

import os
import sys

# read input file into "lines"
input_file = os.path.join(sys.path[0], "example02.txt")
# input_file = os.path.join(sys.path[0], "input02.txt")
with open(input_file) as f:
    lines = f.read().splitlines()
