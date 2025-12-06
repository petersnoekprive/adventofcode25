#!/usr/bin/env python3

import os
import sys

# read input file into "lines"
# input_file = os.path.join(sys.path[0], "example04.txt")
input_file = os.path.join(sys.path[0], "input04.txt")
with open(input_file) as f:
    lines = f.read().splitlines()

def print_lines():
    print("---------------")
    for line in lines:
        print("".join(line))
    print("---------------")

print_lines()   

def has_atsign_at(x, y):
    if y < 0 or y >= len(lines):
        return ""
    if x < 0 or x >= len(lines[y]):
        return ""
    if lines[y][x] == '@':
        return "@"
    return ""

matching_atsigns = []
total_atsigns = 0
iteration_count = 0
atsigns_in_last_iteration = -1

while atsigns_in_last_iteration != 0:

    count_atsign = 0

    for y in range(0, len(lines)):
        line = lines[y]
        print("Line: ", line)
        x_min = 0
        x_max = len(line)
        
        for x in range(0, len(line)):
            char = line[x]
            if char == '@':
                surrounding = (has_atsign_at(x, y-1) + has_atsign_at(x, y+1) + has_atsign_at(x-1, y) + has_atsign_at(x+1, y) + has_atsign_at(x-1, y-1) + has_atsign_at(x+1, y-1) + has_atsign_at(x-1, y+1) + has_atsign_at(x+1, y+1))
                if len(surrounding) < 4:
                    count_atsign += 1
                    matching_atsigns.append((x, y))
                    print("  Found @ at (x,y): ", (x, y), "↑", has_atsign_at(x, y-1), "↓", has_atsign_at(x, y+1), "←", has_atsign_at(x-1, y), "→", has_atsign_at(x+1, y), 
                        "↖", has_atsign_at(x-1, y-1), "↗", has_atsign_at(x+1, y-1), "↙", has_atsign_at(x-1, y+1), "↘", has_atsign_at(x+1, y+1), "surrounding: ", surrounding, "amount: ", len(surrounding))

    # clear the found atsigns
    for x,y in matching_atsigns:
        lines[y] = lines[y][:x] + 'x' + lines[y][x+1:]        

    print_lines()   


    print("---------------")
    total_atsigns += count_atsign
    atsigns_in_last_iteration = count_atsign
    print("@ signs removed: ", count_atsign, " total so far: ", total_atsigns)

    
