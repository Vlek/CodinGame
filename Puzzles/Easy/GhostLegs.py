import math
import sys

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

w, h = [int(i) for i in input().split()]

complete_diagram: list[str] = [input() for i in range(h)]

print("\n".join(complete_diagram), file=sys.stderr, flush=True)

lane_names: list[str] = complete_diagram[0].split()
lanes: list[str] = complete_diagram[1:-1]
output_names: list[str] = complete_diagram[-1].split()

result: list[str] = []

for lane_name_index in range(len(lane_names)):

    current_position: int = lane_name_index * 3 + 1

    for lane in lanes:

        # Check to the left
        if current_position > 0 and lane[current_position - 2] == "-":
            current_position -= 3

        # Check to the right
        elif current_position < w and lane[current_position] == "-":
            current_position += 3

    print(f"Current position: {current_position}", file=sys.stderr, flush=True)

    result.append(
        lane_names[lane_name_index] + output_names[(current_position - 1) // 3]
    )


# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)
for r in result:
    print(r)
