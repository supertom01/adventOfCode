import enum

from day_base import Day


class Day15(Day):

    class Cell(enum.Enum):
        FREE = '.'
        BOX = 'O'
        WALL = '#'

    def __init__(self):
        super().__init__(2024, 15, 'Warehouse Woes', debug=True)

    def parse_data(self):
        grid = []
        current_location = None
        i = 0
        while len(line := self.input[i]) > 0:
            row = []
            for j, x in enumerate(line):
                row.append(self.Cell(x) if x in self.Cell else self.Cell.FREE)
                if x == '@':
                    current_location = (i, j)
            grid.append(row)
            i += 1
        instructions = ''.join(self.input[i:])

        return grid, instructions, current_location
        
    def part_a(self):
        grid, instructions, current_location = self.parse_data()

        for instruction in instructions:
            (i, j) = current_location
            if instruction == '<':
                (di, dj) = (0, -1)
                forward = list(reversed(grid[i][:j]))
            elif instruction == 'v':
                (di, dj) = (1, 0)
                forward = [row[j] for row in grid[i + 1:]]
            elif instruction == '>':
                (di, dj) = (0, 1)
                forward = grid[i][j + 1:]
            else:
                (di, dj) = (-1, 0)
                forward = list(reversed([row[j] for row in grid[:i]]))
            (ti, tj) = (i + di, j + dj)

            # We can just move, easy!
            if grid[ti][tj] == self.Cell.FREE:
                current_location = (ti, tj)
                continue

            # We cannot move through a wall, even easier!
            elif grid[ti][tj] == self.Cell.WALL:
                continue

            # We have to move a box, can we tho?
            if self.Cell.FREE in forward:
                # Check where is the first wall
                first_wall = forward.index(self.Cell.WALL)

                # We can still move. Move the current box to the next free location
                empty_index = forward.index(self.Cell.FREE)

                # We cannot move boxes through a wall, so the free spot should be before the first wall.
                if empty_index < first_wall:
                    grid[ti][tj] = self.Cell.FREE
                    grid[ti + di * empty_index][tj + dj * empty_index] = self.Cell.BOX
                    current_location = (ti, tj)
            else:
                # We cannot move after all.
                continue

        return sum(100 * i + j for i, row in enumerate(grid) for j, x in enumerate(row) if x == self.Cell.BOX)


if __name__ == '__main__':
    (Day15()).run()

