from pathlib import Path
import numpy as np
from collections import ChainMap

lines = ''
with open('input/' + Path(__file__).stem, "r") as text_file:
    lines = text_file.read().splitlines()


def parse_line(line):
    cmd, num = line.split(' ')
    return cmd, int(num.replace('+', ''))


parsed_lines = [parse_line(line) for line in lines]


def part1(input_lines):
    line_index = 0
    accumulator = 0
    visited_lines = []

    while line_index not in visited_lines:
        visited_lines.append(line_index)

        # No infinite loop
        if(line_index >= len(input_lines)):
            return True, accumulator

        cmd, num = input_lines[line_index]

        if(cmd == 'nop'):
            line_index += 1
        elif(cmd == 'acc'):
            accumulator += num
            line_index += 1
        elif(cmd == 'jmp'):
            line_index += num

    return accumulator


def part2():
    for i in range(len(parsed_lines)):
        if(parsed_lines[i][0] == 'acc'):
            continue

        modified_program = parsed_lines.copy()

        val = modified_program[i][1]
        if(parsed_lines[i][0] == 'nop'):
            modified_program[i] = ('jmp', val)
        else:
            modified_program[i] = ('nop', val)

        result = part1(modified_program)
        if(not isinstance(result, int) and result[0] == True):
            print(f'Success: Modified line {i}')
            return result[1]


print(f'Part 1: {part1(parsed_lines)}')
print(f'Part 1: {part2()}')
