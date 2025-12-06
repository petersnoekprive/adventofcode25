#!/usr/bin/env python3

import os
import sys

# read input file into "lines"
# input_file = os.path.join(sys.path[0], "example03.txt")
input_file = os.path.join(sys.path[0], "input03.txt")
with open(input_file) as f:
    lines = f.read().splitlines()

total = 0
for line in lines:
    combinations = []
    print("Line: ", line)
    # iterate over each character in the line, start with first (0) and except the last character (len-1)
    for first_position in range(0, len(line) - 1):
        first = line[first_position] 
        for second_position in range(first_position + 1, len(line)):
            combinations.append(int(str(line[first_position]) + str(line[second_position])))
    print("Combinations : ", combinations)

    combinations.sort(reverse=True)

    answer = str(combinations[0])
    total += int(answer)
    print("Answer for line: ", answer, "total so far: ", total)

print("---------------")
print("ANSWER: ")
