import math
import sys

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

num_appliances, num_button_clicks, max_current_capacity = [
    int(i) for i in input().split()
]

appliances: list[int] = [int(i) for i in input().split()]
appliance_states: list[bool] = [False for i in range(len(appliances))]

power_button_clicks: list[int] = [int(i) for i in input().split()]

# Sanity checks
if len(appliances) != num_appliances:
    print("Appliance numbers do not match", file=sys.stderr, flush=True)

if len(power_button_clicks) != num_button_clicks:
    print("Button clicks do not match", file=sys.stderr, flush=True)

maximal_load: int = 0

for appliance_num in power_button_clicks:

    # Toggle the state of the switch
    appliance_states[appliance_num - 1] = not appliance_states[appliance_num - 1]

    # Calculate current load
    power_used: int = sum(
        [
            appliances[appliance]
            for appliance in range(len(appliances))
            if appliance_states[appliance]
        ]
    )

    if power_used > maximal_load:
        maximal_load = power_used


print(
    f"Appliances: {appliances}\nClicks: {power_button_clicks}",
    file=sys.stderr,
    flush=True,
)
print(
    f"power used: {maximal_load}\nfuse limit: {max_current_capacity}",
    file=sys.stderr,
    flush=True,
)

if maximal_load > max_current_capacity:
    print("Fuse was blown.")
else:
    print("Fuse was not blown.")
    print(f"Maximal consumed current was {maximal_load} A.")
