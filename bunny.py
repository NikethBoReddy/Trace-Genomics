def get_center_cells(grid):
    """
    :param grid: The garden matrix
    :return: A list of the middle cells of the given grid
    """
    rows = len(grid)
    cols = len(grid[0])

    row_mid, col_mid, mid_cells = [], [], []

    # An even number of rows/cols adds in an extra middle cell
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
    """
    :param grid: The garden matrix
    :param cells: The cell locations in the grid whose maximum carrot count needs to be found
    :return: The cell with the maximum carrot count or None if no cells are provided
    """
    curr_max = -1
    curr_max_cell = []
    for cell in cells:
        if grid[cell[0]][cell[1]] > curr_max:
            curr_max = grid[cell[0]][cell[1]]
            curr_max_cell = cell

    # If there are no cells given, to the function, then we return a None value
    # Useful in the case of cells with no neighbors
    if curr_max == -1:
        return None

    return curr_max_cell


def find_neighbors(grid, cell):
    """
    :param grid: The garden matrix
    :param cell: The current cell whose neighbors need to be found
    :return: A list of cell locations that are adjacent to the current cell and within the grid matrix
    """
    curr_row = cell[0]
    curr_col = cell[1]

    rows = len(grid)
    cols = len(grid[0])

    # List all possible neighbors and filter for the valid ones.
    neighbors = [[curr_row-1, curr_col], [curr_row+1, curr_col], [curr_row, curr_col-1], [curr_row, curr_col+1]]
    valid_neighbors = []
    for cell in neighbors:
        if 0 <= cell[0] < rows and 0 <= cell[1] < cols:
            valid_neighbors.append(cell)
    return valid_neighbors


def find_next_cell(grid, cell):
    """
    :param grid: The garden matrix
    :param cell: The current location of the bunny
    :return: Returns the next cell location for the bunny to move to according to the rules, if no such location exits
    it returns None
    """
    neighbors = find_neighbors(grid, cell)
    next_cell = find_max(grid, neighbors)
    if next_cell is not None:
        if grid[next_cell[0]][next_cell[1]] == 0:
            return None
        return next_cell
    return None


def find_carrots_consumed(grid):
    """
    :param grid: The garden matrix
    :return: The number of carrots consumed by the bunny
    """
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
