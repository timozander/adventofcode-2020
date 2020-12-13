from pathlib import Path
import numpy as np
import itertools

lines = ''
with open('input/' + Path(__file__).stem, "r") as text_file:
    lines = text_file.read().splitlines()

values = np.array(lines, dtype=np.int64)

PREAMBLE_LENGTH = 25


def part1():
    for i in range(PREAMBLE_LENGTH, len(values)):
        preamble = values[i - PREAMBLE_LENGTH:i]
        combs = [sum(tpl) for tpl in list(itertools.combinations(preamble, 2))]

        if(values[i] not in combs):
            # invalid
            return i, values[i]


def part2():
    index, val = part1()

    for length in range(2, index + 1):
        for start in range(0, index - length):
            sequence = values[start:start+length]
            s = np.sum(sequence)

            if(s == val):
                return np.sum([np.min(sequence), np.max(sequence)])


print(f'Part 1: {part1()}')
print(f'Part 2: {part2()}')
