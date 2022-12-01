import enum
from copy import deepcopy

from day_base import Day


class Day25(Day):

    class Cucumber(enum.Enum):
        DOWN = 0
        RIGHT = 1
        EMPTY = 2

    def __init__(self):
        super().__init__(2021, 25, 'Sea Cucumber', expected_a=58, debug=False)
        self.grid = []

    def parse(self):
        for row in self.input:
            grid_row = []
            for value in row:
                if value == "v":
                    grid_row.append(Day25.Cucumber.DOWN)
                elif value == ">":
                    grid_row.append(Day25.Cucumber.RIGHT)
                else:
                    grid_row.append(Day25.Cucumber.EMPTY)
            self.grid.append(grid_row)

    def part_a(self) -> int:
        self.parse()

        grid_length = len(self.grid)
        column_length = len(self.grid[0])
        old_grid = []
        counter = 0

        while old_grid != self.grid:
            counter += 1
            old_grid = deepcopy(self.grid)

            # First move right
            for i in range(grid_length):
                for j in range(column_length):
                    cucumber = old_grid[i][j]
                    if cucumber == Day25.Cucumber.RIGHT:
                        if old_grid[i][(j + 1) % column_length] == Day25.Cucumber.EMPTY:
                            self.grid[i][(j + 1) % column_length] = cucumber
                            self.grid[i][j] = Day25.Cucumber.EMPTY

            moved_grid = deepcopy(self.grid)
            # Then move down
            for i in range(grid_length):
                for j in range(column_length):
                    cucumber = moved_grid[i][j]
                    if cucumber == Day25.Cucumber.DOWN:
                        if moved_grid[(i + 1) % grid_length][j] == Day25.Cucumber.EMPTY:
                            self.grid[(i + 1) % grid_length][j] = cucumber
                            self.grid[i][j] = Day25.Cucumber.EMPTY

        return counter


if __name__ == '__main__':
    (Day25()).run()
