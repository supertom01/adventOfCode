from day_base import Day


class Day4(Day):

    def __init__(self):
        super().__init__(2025, 4, 'Printing Department', debug=False, expected_a=13, expected_b=43)

    def part_a(self) -> int:
        grid = [[x for x in row] for row in self.input]
        relative_neighbours = [
            (0, -1),
            (0, 1),
            (-1, 0),
            (-1, 1),
            (-1, -1),
            (1, 0),
            (1, 1),
            (1, -1)
        ]
        accessible_rolls = 0

        for i, row in enumerate(grid):
            for j, x in enumerate(row):
                if x == '@':
                    neighbours = [grid[i + ni][j + nj] for (ni, nj) in relative_neighbours if 0 <= i + ni < len(grid) and 0 <= j + nj < len(row)]
                    paper_neighbours = [x for x in neighbours if x == '@']

                    if len(paper_neighbours) < 4:
                        accessible_rolls += 1
        
        return accessible_rolls
    
    def part_b(self) -> int:
        grid = [[x for x in row] for row in self.input]
        relative_neighbours = [
            (0, -1),
            (0, 1),
            (-1, 0),
            (-1, 1),
            (-1, -1),
            (1, 0),
            (1, 1),
            (1, -1)
        ]
        accessible_rolls = 0
        changed = True

        while changed:
            changed = False
            for i in range(len(grid)):
                row = grid[i]
                for j in range(len(row)):
                    x = grid[i][j]
                    if x == '@':
                        neighbours = [grid[i + ni][j + nj] for (ni, nj) in relative_neighbours if 0 <= i + ni < len(grid) and 0 <= j + nj < len(row)]
                        paper_neighbours = [x for x in neighbours if x == '@']

                        if len(paper_neighbours) < 4:
                            accessible_rolls += 1
                            grid[i][j] = '.'
                            changed = True
        
        return accessible_rolls


if __name__ == '__main__':
    (Day4()).run()
