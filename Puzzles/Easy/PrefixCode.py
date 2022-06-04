import sys

num_prefix_codes = int(input())
prefix_codes: dict[str, str] = {}


for _ in range(num_prefix_codes):

    inputs = input().split()

    binary_code: str = inputs[0]
    ascii_char_num: int = int(inputs[1])

    prefix_codes[binary_code] = chr(ascii_char_num)


encoded_string: str = input()


# Because these have different lengths and we want to make sure that we're
# checking for the largest item first, I will use a sorted list to compare
# our encoded string against.
sorted_prefix_codes: list[str] = sorted(prefix_codes.keys(), key=lambda x: len(x))


# Sanity prints:
print(f"Prefix codes: {prefix_codes}", file=sys.stderr, flush=True)
print(f"Encoded string: {encoded_string}", file=sys.stderr, flush=True)


result_characters: list[str] = []
index: int = 0

while index < len(encoded_string):

    found_code: bool = False

    for code in sorted_prefix_codes:

        if encoded_string[index:].startswith(code):

            result_characters.append(prefix_codes[code])
            index += len(code)

            found_code = True

            continue

    if not found_code:
        result_characters = [f"DECODE FAIL AT INDEX {index}"]
        break


print("".join(result_characters))
