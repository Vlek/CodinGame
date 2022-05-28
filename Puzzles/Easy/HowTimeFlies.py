import math
import sys
from datetime import date, datetime, timedelta

from dateutil import relativedelta

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

beginning_date_timestamp: str = input()
end_date_timestamp: str = input()

start_time: date = datetime.strptime(beginning_date_timestamp, "%d.%m.%Y")
end_time: date = datetime.strptime(end_date_timestamp, "%d.%m.%Y")

time_difference = relativedelta.relativedelta(end_time, start_time)

years: int = time_difference.years
months: int = time_difference.months
days: int = (end_time - start_time).days

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

print(f"Starting timestamp: {beginning_date_timestamp}", file=sys.stderr, flush=True)
print(f"Ending timestamp: {end_date_timestamp}", file=sys.stderr, flush=True)

print(
    (f"{years} year{'s' if years > 1 else ''}, " if years != 0 else "")
    + (f"{months} month{'s' if months > 1 else ''}, " if months != 0 else "")
    + f"total {days} days"
)
