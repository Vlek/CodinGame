import math
import sys

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

w, h, t1, t2, t3 = [int(i) for i in input().split()]

t1_map: list[str] = []
t2_map: list[str] = []
t3_map: list[str] = ["." * w] * h

for i in range(h):
    first_picture_row, second_picture_row = input().split()

    t1_map.append(first_picture_row)
    t2_map.append(second_picture_row)


def get_asteroid_locations(t_map: list[str]) -> dict[str, tuple[int, int]]:

    asteroids: dict[str, tuple[int, int]] = {}

    for row in range(len(t_map)):
        for column in range(w):

            map_spot = t_map[row][column]
            if map_spot != ".":

                asteroids[map_spot] = (column, row)

    return asteroids


asteroids_at_t1: dict[str, tuple[int, int]] = get_asteroid_locations(t1_map)
asteroids_at_t2: dict[str, tuple[int, int]] = get_asteroid_locations(t2_map)

print(f"asteroids for map at t1: {asteroids_at_t1}", file=sys.stderr, flush=True)
print(f"asteroids for map at t2: {asteroids_at_t2}", file=sys.stderr, flush=True)

# Sanity printing:

print(f"T1: {t1}, T2: {t2}, T3: {t3}", file=sys.stderr, flush=True)
first_picture_string = "\n".join(t1_map)
second_picture_string = "\n".join(t2_map)

print(f"First picture:\n{first_picture_string}", file=sys.stderr, flush=True)
print(f"Second picture:\n{second_picture_string}", file=sys.stderr, flush=True)

t1_t2_time_diff: int = t2 - t1
t2_t3_time_diff: int = t3 - t2

time_delta: float = t2_t3_time_diff / t1_t2_time_diff

for asteroid in reversed(sorted(asteroids_at_t1.keys())):
    print(f"Handling asteroid: {asteroid}", file=sys.stderr, flush=True)

    # These are starting from t2 since that's where we're technically starting from for t3
    t1_x_position: int = asteroids_at_t1[asteroid][0]
    t1_y_position: int = asteroids_at_t1[asteroid][1]

    t2_x_position: int = asteroids_at_t2[asteroid][0]
    t2_y_position: int = asteroids_at_t2[asteroid][1]

    x_movement: int = t2_x_position - t1_x_position
    y_movement: int = t2_y_position - t1_y_position

    t3_x_position = t2_x_position + math.floor(x_movement * time_delta)
    t3_y_position = t2_y_position + math.floor(y_movement * time_delta)

    # If the asteroid is still within the bounds of the map,
    if 0 <= t3_y_position < h and 0 <= t3_x_position < w:
        map_row = t3_map[t3_y_position]

        t3_map[t3_y_position] = (
            map_row[:t3_x_position] + asteroid + map_row[t3_x_position + 1 :]
        )

print(f"\n\nPrinting answer:", file=sys.stderr, flush=True)
for section in t3_map:
    print(section)
