from pathlib import Path
import numpy as np
from collections import ChainMap
import re

# input_matrix = np.array([list(line) for line in lines])

file = ''
with open('input/' + Path(__file__).stem, "r") as text_file:
    file = text_file.read()

lines = np.array([passport.replace('\n', ' ')
                  for passport in file.split('\n\n')])


lines = np.array(
    [dict(ChainMap(*list(map(lambda elem: dict([elem.split(':')]), line.split(' ')))))
     for line in lines]
)

required_keys = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
optional_keys = ['cid']


def validation_fn1(l): return all(key in l for key in required_keys)


def is_valid_height(height):
    if(height.endswith('cm')):
        h = int(height.replace('cm', ''))
        return h >= 150 and h <= 193
    elif(height.endswith('in')):
        h = int(height.replace('in', ''))
        return h >= 59 and h <= 76
    return False


hair_color_pattern = re.compile("^#[a-f0-9]{6}$")
pid_pattern = re.compile("^[0-9]{9}$")


def validation_fn2(l):
    return (all(key in l for key in required_keys) and
            int(l['byr']) >= 1920 and int(l['byr']) <= 2002 and
            int(l['iyr']) >= 2010 and int(l['iyr']) <= 2020 and
            int(l['eyr']) >= 2020 and int(l['eyr']) <= 2030 and
            is_valid_height(l['hgt']) and
            hair_color_pattern.match(l['hcl']) and
            l['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'] and
            pid_pattern.match(l['pid']))


def solve(fn):
    return list(filter(fn, lines))


print(f'Part 1: {len(solve(validation_fn1))}')
print(f'Part 2: {len(solve(validation_fn2))}')
