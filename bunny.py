def get_center_cells(grid):
    """
    Returns a list of the middle cells given a grid
    :param grid:
    :return:
    """
    rows = len(grid)
    cols = len(grid[0])

    row_mid, col_mid, mid_cells = [], [], []
    if rows % 2 == 0:
        row_mid.append(int((rows/2) - 1))
    row_mid.append(int(rows/2))
    if cols % 2 == 0:
        col_mid.append(int((cols/2) - 1))
    col_mid.append(int(cols/2))

    for row in row_mid:
        for col in col_mid:
            mid_cells.append([row, col])
    return mid_cells


def find_max(grid, cells):
    curr_max = -1
    curr_max_cell = []
    for cell in cells:
        if grid[cell[0]][cell[1]] > curr_max:
            curr_max = grid[cell[0]][cell[1]]
            curr_max_cell = cell

    if curr_max == -1:
        return None

    return curr_max_cell


def find_neighbors(grid, cell):
    curr_row = cell[0]
    curr_col = cell[1]

    rows = len(grid)
    cols = len(grid[0])

    neighbors = [[curr_row-1, curr_col], [curr_row+1, curr_col], [curr_row, curr_col-1], [curr_row, curr_col+1]]
    valid_neighbors = []
    for cell in neighbors:
        if 0 <= cell[0] < rows and 0 <= cell[1] < cols:
            valid_neighbors.append(cell)
    return valid_neighbors


def find_next_cell(grid, cell):
    neighbors = find_neighbors(grid, cell)
    next_cell = find_max(grid, neighbors)
    if next_cell is not None:
        if grid[next_cell[0]][next_cell[1]] == 0:
            return None
        return next_cell
    return None


def find_carrots_consumed(grid):
    if grid is None or len(grid) == 0 or len(grid[0]) == 0:
        return 0

    mid_cells = get_center_cells(grid)
    curr_cell = find_max(grid, mid_cells)
    carrots_consumed = 0

    while curr_cell is not None:
        carrots_consumed += grid[curr_cell[0]][curr_cell[1]]
        grid[curr_cell[0]][curr_cell[1]] = 0
        curr_cell = find_next_cell(grid, curr_cell)

    return carrots_consumed
