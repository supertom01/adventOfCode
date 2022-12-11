import numpy as np

from day_base import Day


def is_visible(grid, grid_transpose, i, j):
    if i == 0 or i == len(grid) - 1 or j == 0 or j == len(grid[0]) - 1:
        return True

    return max(grid[i][:j]) < grid[i][j] or max(grid[i][j+1:]) < grid[i][j] \
        or max(grid_transpose[j][:i]) < grid_transpose[j][i] or max(grid_transpose[j][i+1:]) < grid_transpose[j][i]


def calculate_scenic_score(grid, grid_transpose, i, j):
    tree = grid[i][j]
    width = len(grid_transpose)
    height = len(grid)

    if i == 0 or i == height - 1 or j == 0 or j == width - 1:
        return 0

    scenic_score = 1
    # Look left
    temp = 0
    for k in range(1, j + 1):
        if grid[i][j - k] < tree:
            temp += 1
        else:
            temp += 1
            break
    scenic_score *= temp

    # Look right
    temp = 0
    for k in range(1, width - j):
        if grid[i][j + k] < tree:
            temp += 1
        else:
            temp += 1
            break
    scenic_score *= temp

    # Look up
    temp = 0
    for k in range(1, i + 1):
        if grid_transpose[j][i - k] < tree:
            temp += 1
        else:
            temp += 1
            break
    scenic_score *= temp

    # Look down
    temp = 0
    for k in range(1, height - i):
        if grid_transpose[j][i + k] < tree:
            temp += 1
        else:
            temp += 1
            break
    scenic_score *= temp
    return scenic_score


class Day8(Day):

    def __init__(self):
        super().__init__(2022, 8, 'Treetop Tree House', expected_a=21, expected_b=8, debug=False)

    def parse(self):
        return [[int(x) for x in row] for row in self.input]

    def part_a(self) -> int:
        grid = self.parse()
        grid_transpose = np.transpose(grid)
        return sum(sum(1 for j in range(len(grid[i])) if is_visible(grid, grid_transpose, i, j)) for i in range(len(grid)))

    def part_b(self) -> int:
        grid = self.parse()
        grid_transpose = np.transpose(grid)
        return max(max(calculate_scenic_score(grid, grid_transpose, i, j) for j in range(len(grid_transpose))) for i in range(len(grid)))


if __name__ == '__main__':
    (Day8()).run()
