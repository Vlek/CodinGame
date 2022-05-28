import math
import sys

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

line_1 = input()
line_2 = input()
line_3 = input()

#  _     _  _     _  _  _  _  _
# | |  | _| _||_||_ |_   ||_||_|
# |_|  ||_  _|  | _||_|  ||_| _|
ascii_numbers: dict[str, int] = {
    " _ | ||_|": 0,
    "     |  |": 1,
    " _  _||_ ": 2,
    " _  _| _|": 3,
    "   |_|  |": 4,
    " _ |_  _|": 5,
    " _ |_ |_|": 6,
    " _   |  |": 7,
    " _ |_||_|": 8,
    " _ |_| _|": 9,
}

# Find the answer
result_numbers: list[int] = []

for index in range(0, len(line_1), 3):

    current_number_string = (
        line_1[index : index + 3]
        + line_2[index : index + 3]
        + line_3[index : index + 3]
    )

    result_numbers.append(ascii_numbers[current_number_string])


# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)
print("".join([str(i) for i in result_numbers]))
