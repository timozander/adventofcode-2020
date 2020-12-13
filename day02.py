from pathlib import Path
import numpy as np

lines = np.genfromtxt('input/' + Path(__file__).stem,
                      delimiter=':', dtype='str')

# print(lines[0, :])


def part1(lines):
    res = np.char.split(lines[:, 0], sep=' ')
    res = np.array(list(map(lambda l: np.array(l), res)))

    rules, character = np.hsplit(res, 2)

    rules = np.char.split(rules.ravel(), sep='-')
    rules = np.array(list(map(lambda l: (int(l[0]), int(l[1])), rules)))
    character = character.ravel()

    count = np.char.count(lines[:, 1], character)

    return ((count >= rules[:, 0]) & (count <= rules[:, 1]))


def part2(lines):
    res = np.char.split(lines[:, 0], sep=' ')
    res = np.array(list(map(lambda l: np.array(l), res)))

    rules, character = np.hsplit(res, 2)

    rules = np.char.split(rules.ravel(), sep='-')
    rules = np.array(list(map(lambda l: (int(l[0]), int(l[1])), rules)))
    character = character.ravel()

    width = max(len(w) for w in np.char.lstrip(lines[:, 1]))
    password_matrix = np.array([list(word.ljust(width))
                                for word in np.char.lstrip(lines[:, 1])])
    password_matrix = (np.stack(password_matrix))

    # print(rules[:, 0])
    # print(password_matrix[:, 0])

    first_char = (password_matrix[np.arange(
        len(password_matrix)), rules[:, 0] - 1])
    secnd_char = (password_matrix[np.arange(
        len(password_matrix)), rules[:, 1] - 1])

    char_matrix = np.vstack((first_char, secnd_char)).T

    return ((char_matrix[:, 0] != char_matrix[:, 1]) & (
        (char_matrix[:, 0] == character) | (char_matrix[:, 1] == character)))


print(f'Part 1: {np.count_nonzero(part1(lines))}')
print(f'Part 2: {np.count_nonzero(part2(lines))}')

# print(lines[mask(lines[:, 0], lines[:, 1]) == True])
