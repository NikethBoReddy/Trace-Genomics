from bunny import find_carrots_consumed

null_garden = None
null_row_garden = []
null_col_garden = [[], []]
cell_garden = [[1]]
row_garden_single_mid = [[1, 2, 0, 4, 5]]
row_garden_double_mid = [[1, 2, 3, 5, 2, 0]]
col_garden_single_mid = [[1], [2], [0], [4], [5]]
col_garden_double_mid = [[1], [2], [3], [5], [2], [0]]
garden_zeros = \
    [[0, 0, 0],
     [0, 0, 0],
     [0, 0, 0]]
garden_four_mid = \
    [[1, 2, 3, 9],
     [0, 2, 9, 1],
     [1, 7, 0, 1],
     [9, 7, 1, 2]]
test_garden = \
    [[5, 7, 8, 6],
     [0, 0, 7, 0],
     [4, 6, 3, 4],
     [3, 1, 0, 5]]

with open('matrix.txt', 'r') as f:
    file_garden = [[int(num) for num in line.split(',')] for line in f]

assert (0 == find_carrots_consumed(null_garden))
assert (0 == find_carrots_consumed(null_row_garden))
assert (0 == find_carrots_consumed(null_col_garden))
assert (1 == find_carrots_consumed(cell_garden))
assert (9 == find_carrots_consumed(row_garden_single_mid))
assert (11 == find_carrots_consumed(row_garden_double_mid))
assert (9 == find_carrots_consumed(col_garden_single_mid))
assert (11 == find_carrots_consumed(col_garden_double_mid))
assert (0 == find_carrots_consumed(garden_zeros))
assert (55 == find_carrots_consumed(garden_four_mid))
assert (27 == find_carrots_consumed(test_garden))
assert (12 == find_carrots_consumed(file_garden))
