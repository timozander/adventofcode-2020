from pathlib import Path
import numpy as np

lines = np.genfromtxt('input/' + Path(__file__).stem,
                      delimiter='', comments=None, dtype='str')

input_matrix = np.array([list(line) for line in lines])

# print(lines[0, :])


def solve(slope_right=3, slope_down=1):
    width = input_matrix.shape[1]

    n = np.arange(int(input_matrix.shape[0]/slope_down))
    hit_elements = input_matrix[n * slope_down, (n * slope_right) % width]

    unique, counts = np.unique(hit_elements, return_counts=True)
    return dict(zip(unique, counts))['#']


def part2():
    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    trees = []
    for slope in slopes:
        trees.append(solve(slope[0], slope[1]))

    return np.prod(trees)


print(f'Part 1: {solve()}')
print(f'Part 2: {part2()}')

# print(lines[mask(lines[:, 0], lines[:, 1]) == True])
