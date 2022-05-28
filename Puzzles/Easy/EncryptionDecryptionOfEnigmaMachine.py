import math
import sys

operation = input()

pseudo_random_number = int(input())

rotors: list[str] = [input() for i in range(3)]

message = input()

print(f"Operation: {operation}", file=sys.stderr, flush=True)
print(f"Starting num: {pseudo_random_number}", file=sys.stderr, flush=True)
print(f"Rotors: {rotors}", file=sys.stderr, flush=True)
print(f"Starting message: {message}\n", file=sys.stderr, flush=True)

output = []

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def character_rotator(characters, rotor):
    result = []

    for character_index in range(len(characters)):
        character_number = alphabet.index(characters[character_index])

        result.append(rotor[character_number])

    return result


def decode_rotator(characters, rotor):
    result = []

    for character_index in range(len(characters)):
        character_number = rotor.index(characters[character_index])

        result.append(alphabet[character_number])

    return result


def caesar_cipher(message, random_number):
    result = []
    for character_index in range(len(message)):
        rotation_number = random_number + character_index
        character = message[character_index]
        index_in_alphabet = alphabet.index(character)

        result.append(alphabet[(index_in_alphabet + rotation_number) % 26])

    return result


def decode_caesar_cipher(message, random_number):
    result = []
    for character_index in range(len(message)):
        rotation_number = (random_number + character_index) * -1
        character = message[character_index]
        index_in_alphabet = alphabet.index(character)

        result.append(alphabet[(index_in_alphabet + rotation_number) % 26])

    return result


if operation == "ENCODE":

    output = caesar_cipher(message, pseudo_random_number)

    print(output, file=sys.stderr, flush=True)

    # Do rotations with rotors
    for rotation in rotors:
        output = character_rotator(output, rotation)

else:
    output = [c for c in message]

    for rotation in reversed(rotors):
        output = decode_rotator(output, rotation)

        print("Output: " + "".join(output), file=sys.stderr, flush=True)

    output = decode_caesar_cipher(output, pseudo_random_number)


print("\nResult:", file=sys.stderr, flush=True)
print("".join(output))
