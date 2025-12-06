#!/usr/bin/env python3

import os
import sys

# read input file into "lines"
# input_file = os.path.join(sys.path[0], "example04.txt")
input_file = os.path.join(sys.path[0], "input04.txt")
with open(input_file) as f:
    lines = f.read().splitlines()

def has_atsign_at(x, y):
    if y < 0 or y >= len(lines):
        return ""
    if x < 0 or x >= len(lines[y]):
        return ""
    if lines[y][x] == '@':
        return "@"
    return ""

count_atsign = 0
for y in range(0, len(lines)):
    line = lines[y]
    print("Line: ", line)
    x_min = 0
    x_max = len(line)
    
    for x in range(0, len(line)):
        char = line[x]
        if char == '@':
            surrounding = (
                has_atsign_at(x, y-1) +
                has_atsign_at(x, y+1) +
                has_atsign_at(x-1, y) +
                has_atsign_at(x+1, y) +
                has_atsign_at(x-1, y-1) +
                has_atsign_at(x+1, y-1) +
                has_atsign_at(x-1, y+1) +
                has_atsign_at(x+1, y+1)
            )
            if len(surrounding) < 4:
                count_atsign += 1
            print("  Found @ at (x,y): ", (x, y), "↑", has_atsign_at(x, y-1), "↓", has_atsign_at(x, y+1), "←", has_atsign_at(x-1, y), "→", has_atsign_at(x+1, y), 
                  "↖", has_atsign_at(x-1, y-1), "↗", has_atsign_at(x+1, y-1), "↙", has_atsign_at(x-1, y+1), "↘", has_atsign_at(x+1, y+1), "surrounding: ", surrounding, "amount: ", len(surrounding))
    
    


print("---------------")
print("ANSWER: ", count_atsign)
