#!/usr/bin/env python3

import os
import sys

# read input file into "lines"
# input_file = os.path.join(sys.path[0], "example03.txt")
input_file = os.path.join(sys.path[0], "input03.txt")
with open(input_file) as f:
    lines = f.read().splitlines()

# clear the console
os.system('clear')

total = 0
answers = []
for line in lines:
    # print("Line: ", line, "  Line length: ", len(line))

    battery_count = 0
    max_battery = 12
    total = 0
    start = 0
    number_string = ""

    for battery in range(0, max_battery):
        end = len(line) - max_battery + battery
        search_line_part = line[start:end+1]
        # print("  Battery ", battery)
        # print("    Searching", line, "between positions", start, "and", end, "=", search_line_part)
        # find the highest digit in the part of the line, starting with battery and ending remaining characters from the end
        highest_digit = -1
        position_of_highest = -1
        for digit in search_line_part:
            if int(digit) > highest_digit:
                highest_digit = int(digit)
                
                
        # print("    Highest digit in this range: ", highest_digit)
        # find the first occurrance of the highest digit in the same range
        for position in range(start, end+1):
            digit = int(line[position])
            if digit == highest_digit:
                # print("    Found first occurance of highest digit ", highest_digit, " at position ", position)
                start = position + 1
                number_string += str(highest_digit)
                break
        # print("    Number so far: ", number_string)

    line_answer = number_string
    total += int(line_answer)
    answers.append(int(line_answer))
    print("  Answer: ", line_answer, "int value: ", int(line_answer), "total so far: ", total)

print("---------------")
print("All answers: ", answers)
total = sum(answers)
print("ANSWER: ", str(total))
