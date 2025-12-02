#!/usr/bin/env python3

import os
import sys

# read input file into "lines"
# input_file = os.path.join(sys.path[0], "example02.txt")
input_file = os.path.join(sys.path[0], "input02.txt")
with open(input_file) as f:
    lines = f.read().splitlines()


def sum_false_ids_in_range(range_str):
    count = 0
    start, end = map(int, range_str.split("-"))
    for i in range(start, end + 1):
        # check if i has a even number of digits, like 2, 4, 6, 8 etc.
        if len(str(i)) % 2 == 0:
            # cast i to string and split into two halves, and check if both halves are the same
            # e.g. 1221 -> "12" and "21" -> not the same
            # e.g. 11 -> "1" and "1" -> the same
            str_i = str(i)
            half = len(str_i) // 2
            if str_i[:half] == str_i[half:]:
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
        total += sum_false_ids_in_range(item)

print("---------------")
print("Total count of false IDs: ", total)