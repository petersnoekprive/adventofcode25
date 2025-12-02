#!/usr/bin/env python3

import os
import sys
import re

# read input file into "lines"
# input_file = os.path.join(sys.path[0], "example02.txt")
input_file = os.path.join(sys.path[0], "input02.txt")
with open(input_file) as f:
    lines = f.read().splitlines()


def is_repeating(s):
    return bool(re.match(r"^(.+)\1+$", s))

def count_false_ids_in_range(range_str):
    count = 0
    start, end = map(int, range_str.split("-"))
    for i in range(start, end + 1):
        if is_repeating(str(i)):
            count += i
            print("  Found false ID: ", i)
    return count

parts = []
for line in lines:
    print("Line: ", line)
    parts.append(line.split(","))

print("---------------")
print("PARTS: ")
total = 0
for part in parts:
    for item in part:
        print(item)
        total += count_false_ids_in_range(item)

print("---------------")
print("Total count of false IDs: ", total)