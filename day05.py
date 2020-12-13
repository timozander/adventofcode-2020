from pathlib import Path
import numpy as np

lines = np.genfromtxt('input/' + Path(__file__).stem,
                      delimiter='', comments=None, dtype='str')

row_count = 128
col_count = 8


def binary_split(str, upper, lower, count):
    items = np.arange(0, count)
    for char in str:
        parts = np.split(items, 2)
        if(char == upper):
            items = parts[1]
        elif(char == lower):
            items = parts[0]

    assert len(items) == 1
    return items[0]


def parse_seat(coord):
    row_coord = coord[0:7]
    col_coord = coord[7:]

    # Determine row
    row = binary_split(row_coord, 'B', 'F', row_count)

    # Determine col
    col = binary_split(col_coord, 'R', 'L', col_count)

    return (row, col)


def seat_id(seat_tuple):
    return seat_tuple[0] * 8 + seat_tuple[1]


seats = [parse_seat(coord) for coord in lines]
seat_ids = [seat_id(seat) for seat in seats]

# Test
assert parse_seat("BFFFBBFRRR") == (70, 7)
assert seat_id((70, 7)) == 567

print(np.sort(seat_ids))

# Part 2
p2_seats = [seat for seat in seats if seat[0]
            != 0 and seat[0] != row_count - 1]
p2_seat_ids = np.sort([seat_id(seat) for seat in p2_seats])

p2_min = np.min(p2_seat_ids)
p2_max = np.max(p2_seat_ids)

all_seats = np.arange(p2_min, p2_max + 1)


print(f'Part 1: {max(seat_ids)}')
print(f'Part 2: {np.setdiff1d(all_seats, p2_seat_ids)[0]}')
