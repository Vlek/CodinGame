import math
import sys

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

last_river_one_value = int(input())
last_river_two_value = int(input())

river_one: dict[int, int] = {last_river_one_value: 0}
river_two: dict[int, int] = {last_river_two_value: 0}


def get_next_river_value(river):
    return river + sum([int(i) for i in str(river)])


def get_common_values(river1: dict[int, int], river2: dict[int, int]):
    return [i for i in river1 if i in river2]


def latest_value_in_other_river(value: int, other_river: dict[int, int]):
    return value in other_river


common_values: list[int] = []

while len(common_values) == 0:

    last_river_one_value = get_next_river_value(last_river_one_value)
    last_river_two_value = get_next_river_value(last_river_two_value)

    river_one[last_river_one_value] = 0
    river_two[last_river_two_value] = 0

    if latest_value_in_other_river(last_river_one_value, river_two):
        common_values.append(last_river_one_value)

    elif latest_value_in_other_river(last_river_two_value, river_one):
        common_values.append(last_river_two_value)

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)
print(common_values[0])
