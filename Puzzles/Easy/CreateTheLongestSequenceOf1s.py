import math
import sys

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

bit_string = input()


def count_num_ones_in_a_row(bit_string) -> int:
    """Returns the length of the longest sequence of 1's."""

    longest_ones_row: int = 0

    current_ones_row: int = 0

    for b in bit_string:
        if b == "1":
            current_ones_row += 1
        else:
            current_ones_row = 0

        if current_ones_row > longest_ones_row:
            longest_ones_row = current_ones_row

    return longest_ones_row


longest_ones_count: int = 0

for index in range(len(bit_string)):
    if bit_string[index] == "0":
        new_bit_string: str = bit_string[:index] + "1" + bit_string[index + 1 :]

        current_ones_count: int = count_num_ones_in_a_row(new_bit_string)

        if current_ones_count > longest_ones_count:
            longest_ones_count = current_ones_count


# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)
print(longest_ones_count)
