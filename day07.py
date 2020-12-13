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


def rule_bfs_amounts(key, rules):
    visited = []
    must_contain = []
    allowed_colors = rules[key]

    while len(allowed_colors) > 0:
        col, amount = allowed_colors.pop()

        rule = [(item[0], item[1] * amount)
                for item in rules[col] if item not in visited]

        allowed_colors.extend(rule)
        must_contain.append((col, amount))
        visited.append(col)

    return must_contain


rules = dict(ChainMap(*[parse_rule(line) for line in lines]))

# Part 1
# bfs_rules = []
# for k in rules.keys():
#     bfs_rules.append(rule_bfs(k, rules))

# shiny_rules = list(filter(lambda r: 'shiny gold' in r, bfs_rules))
# print(f'Part 1: {len(shiny_rules)}')


shiny_rule_amount = rule_bfs_amounts('shiny gold', rules)
sumed_amount = sum([item[1] for item in shiny_rule_amount])
print(shiny_rule_amount)
print(f'Part 2: {sumed_amount}')
