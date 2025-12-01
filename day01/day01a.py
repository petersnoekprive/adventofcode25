#!/usr/bin/env python3

import os
import sys

# read input file into "lines"
# input_file = os.path.join(sys.path[0], "example01.txt")
input_file = os.path.join(sys.path[0], "input01.txt")
with open(input_file) as f:
    lines = f.read().splitlines()


def dial_left(position, amount):
    for i in range(amount):
        position = position - 1
        if position < 0:
            position = 99
    return position

def dial_right(position, amount):
    for i in range(amount):
        position = position + 1
        if position > 99:
            position = 0
    return position

actual_position = 50
amount_zeroes = 0
print("Initial position: ", actual_position)
for line in lines:
    print("Line: ", line)
    if line[0] == 'L':
        actual_position = dial_left(actual_position, int(line[1:]))
    elif line[0] == 'R':
        actual_position = dial_right(actual_position, int(line[1:]))
    if actual_position == 0:
        amount_zeroes += 1
        print("  Hit zero! Total so far: ", amount_zeroes)
    print("  New position: ", actual_position)

print("---------------")
print("ANSWER: ", amount_zeroes)
