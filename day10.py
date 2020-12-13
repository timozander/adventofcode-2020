from pathlib import Path
import numpy as np
import itertools

lines = ''
with open('input/' + Path(__file__).stem, "r") as text_file:
    lines = text_file.read().splitlines()

adapters = np.array(lines, dtype=int)

device_jol = np.max(adapters) + 3


def part1():
    jol = 0
    difference = {
        1: 0,
        2: 0,
        3: 0
    }
    while jol < device_jol:
        # Find matching adapter
        possible_adapter = np.sort(
            adapters[(adapters - jol <= 3) & (adapters - jol > 0)])

        # Arrived at device
        if(len(possible_adapter) == 0):
            difference[3] += 1
            break

        adapter = possible_adapter[0]
        difference[adapter - jol] += 1
        jol = adapter

    print(difference)
    return difference[1] * difference[3]


def part2(jol=0, prev=[]):
    current_jol = jol

    if(current_jol == device_jol):
        return []

    # Find matching adapter
    possible_adapter = np.sort(
        adapters[(adapters - jol <= 3) & (adapters - jol > 0)])

    # Arrived at device
    # if(len(possible_adapter) == 0):
    #     return []

    return prev + [part2(adapt,  [adapt]) for adapt in possible_adapter]


def count_paths(tree):
    if(not isinstance(tree, list)):
        return int(tree == device_jol - 3)

    return np.sum([count_paths(subtree) for subtree in tree])


print(f'Device: {device_jol} joltage')
# print(f'Part 1: {part1()}')
tree = part2()
paths = count_paths(tree)
print(f'Part 2: {paths}')
