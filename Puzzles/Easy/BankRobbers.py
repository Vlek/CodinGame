import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

num_robbers: int = int(input())

num_vaults: int = int(input())

vaults: list[list[int]] = []

for i in range(num_vaults):
    c, n = [int(j) for j in input().split()]

    vaults.append([c, n])


total_time_required: int = 0

# Sanity prints:
print(f"Num robbers: {num_robbers}", file=sys.stderr, flush=True)
print(f"Vaults: {vaults}", file=sys.stderr, flush=True)

# 0-9
num_digits: int = 10
# A, E, I, O, and U
num_vowels: int = 5

vault_completion_times: list[int] = []

for vault in vaults:

    # N is the digit portion of the vault combination
    digit_portion_length: int = vault[1]

    # The C portion appears to be the total length of the combination.
    # To get the vowel portion, we take away the digit portion.
    vowel_portion_length: int = vault[0] - vault[1]

    # https://math.stackexchange.com/a/2285644
    total_time_required: int = (num_digits ** digit_portion_length) * (num_vowels ** vowel_portion_length)

    vault_completion_times.append(total_time_required)

# This gets us much closer but isn't correct. We're ever so slightly off on test #4
# vault_completion_times.sort()

print(f"Vault completion times: {vault_completion_times}", file=sys.stderr, flush=True)


# Here's where we have to remove time based on how many robbers are present.
#
# The issue is that we're interested in the total time for the group, not how
# long it would take them all sequentially to complete.
#
# To this end, I think we should only really care about the time taken for
# the person that takes the longest time.
total_time_taken: int = 0

for start_vault_index in range(0, len(vaults), num_robbers):

    longest_time_per_robber: int = 0

    for vault_index in range(num_robbers):

        current_vault_index: int = vault_index + start_vault_index

        current_completion_time: int = vault_completion_times[current_vault_index]

        if current_completion_time > longest_time_per_robber:
            longest_time_per_robber = current_completion_time

    total_time_taken += longest_time_per_robber

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)
print(total_time_taken)
