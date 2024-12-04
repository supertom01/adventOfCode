from day_base import Day


class Day4(Day):

    def __init__(self):
        super().__init__(2024, 4, 'Ceres Search', expected_a=18, expected_b=9, debug=False)
        
    def part_a(self):
        matrix = [[x for x in row] for row in self.input]
        row_len = len(matrix)
        col_len = len(matrix[0])

        count = 0
        for i, row in enumerate(matrix):
            for j, char in enumerate(row):

                if char == 'X':
                    directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, 1), (1, -1), (-1, -1), (1, 1)]
                    directions = [(di, dj) for (di, dj) in directions if 0 <= i + di < row_len and 0 <= j + dj < col_len and matrix[i + di][j + dj] == 'M']
                    directions = [(di, dj) for (di, dj) in directions if 0 <= i + di * 2 < row_len and 0 <= j + dj * 2 < col_len and matrix[i + di * 2][j + dj * 2] == 'A']
                    directions = [(di, dj) for (di, dj) in directions if 0 <= i + di * 3 < row_len and 0 <= j + dj * 3 < col_len and matrix[i + di * 3][j + dj * 3] == 'S']
                    count += len(directions)

        return count

    def part_b(self) -> int:
        matrix = [[x for x in row] for row in self.input]
        row_len = len(matrix)
        col_len = len(matrix[0])

        count = 0
        for i, row in enumerate(matrix):
            for j, char in enumerate(row):

                # Find all A and make sure the S and the M are aligned properly around it.
                if char == 'A':
                    directions = [(-1, 1), (1, -1), (-1, -1), (1, 1)]
                    chars = [matrix[i + di][j + dj] for (di, dj) in directions if
                             0 <= i + di < row_len and 0 <= j + dj < col_len]
                    if len(chars) != 4:
                        continue

                    if 'M' in chars[:2] and 'S' in chars[:2] and 'M' in chars[2:] and 'S' in chars[2:]:
                        count += 1
        return count

    def part_b_oneliner(self) -> int:
        return sum(1 for i, row in enumerate(self.input) for j, char in enumerate(row) if char == 'A' and (chars := [self.input[i + di][j + dj] for (di, dj) in [(-1, 1), (1, -1), (-1, -1), (1, 1)] if 0 <= i + di < len(self.input) and 0 <= j + dj < len(self.input[0])]) and len(chars) == 4 and ('M' in chars[:2] and 'S' in chars[:2] and 'M' in chars[2:] and 'S' in chars[2:]))


if __name__ == '__main__':
    (Day4()).run()

