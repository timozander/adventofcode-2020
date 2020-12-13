from pathlib import Path
import numpy as np
from collections import ChainMap

lines = ''
with open('input/' + Path(__file__).stem, "r") as text_file:
    lines = text_file.read().splitlines()


def parse_rule(line):
    [color, contents] = line.split(' bags contain ')

    rule = dict()
    rule[color] = []

    if(contents == 'no other bags.'):
        return rule

    content_colors = contents.replace('.', '').replace(
        'bag,', 'bags,').split(' bags, ')

    for col in content_colors:
        [amount, curr_col] = col.split(' ', 1)
        rule[color].append(
            (curr_col.replace('bags', '').replace('bag', '').strip(), int(amount)))

    return rule


def rule_bfs(key, rules):
    visited = []
    allowed_colors = [key]

    while len(allowed_colors) > 0:
        col = allowed_colors.pop()

        if(col in visited):
            continue

        rule = [item[0] for item in rules[col] if item not in visited]

        allowed_colors.extend(rule)
        visited.append(col)

    visited.remove(key)
    return visited


rules = dict(ChainMap(*[parse_rule(line) for line in lines]))

bfs_rules = []
for k in rules.keys():
    bfs_rules.append(rule_bfs(k, rules))

shiny_rules = list(filter(lambda r: 'shiny gold' in r, bfs_rules))
print(f'Part 1: {len(shiny_rules)}')


# print(f'Part 1: {max(seat_ids)}')
# print(f'Part 2: {np.setdiff1d(all_seats, p2_seat_ids)[0]}')
