import math
import sys

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

gymnasts: list[str] = input().split(",")

categories: list[str] = input().split(",")

number_of_records = int(input())

records: list[str] = [input() for _ in range(number_of_records)]

# Sanity prints:
print(f"Gymnasts: {gymnasts}", file=sys.stderr, flush=True)
print(f"Categories: {categories}", file=sys.stderr, flush=True)
print(f"Records: {records}", file=sys.stderr, flush=True)


gymnast_records: dict[str, dict[str, float]] = {gymnast: {} for gymnast in gymnasts}

for record in records:

    record_info: list[str] = record.split(",")

    print(f"Record info: {record_info}", file=sys.stderr, flush=True)

    gymnast: str = record_info[0]

    if gymnast not in gymnast_records:
        continue

    scores: dict[str, float] = {
        "bars": float(record_info[1]),
        "beam": float(record_info[2]),
        "floor": float(record_info[3]),
    }

    for category in categories:

        if category not in gymnast_records[gymnast]:
            gymnast_records[gymnast][category] = scores[category]
        else:
            if scores[category] > gymnast_records[gymnast][category]:
                gymnast_records[gymnast][category] = scores[category]


print(f"Gymnast Highest Scores: {gymnast_records}", file=sys.stderr, flush=True)


def format_record(rec: float) -> str:
    if rec % 1 != 0:
        return str(rec)
    else:
        return f"{rec:.0f}"


# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)
for gymnast in gymnasts:

    output: list[str] = []

    for category in categories:
        output.append(format_record(gymnast_records[gymnast][category]))

    print(",".join(output))
