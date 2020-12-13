import numpy as np
import itertools

lines = np.loadtxt("input/day01")


def solution(r):
    mesh = np.array(list(itertools.combinations(lines, r)))
    result = mesh[mesh.sum(axis=1) == 2020][0]
    return (result, np.prod(result))


print(f'Part 1: {solution(2)}')
print(f'Part 2: {solution(3)}')
