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

        # Find all MAS
        found_mas: dict[tuple[int, int], list[tuple[int, int]]] = dict()
        direction_to_coordinate: dict[tuple[int, int], list[tuple[int, int]]] = dict()
        for direction in [(-1, 1), (1, -1), (-1, -1), (1, 1)]:
            direction_to_coordinate[direction] = []

        for i, row in enumerate(matrix):
            for j, char in enumerate(row):
                if char == 'M':
                    directions = [(-1, 1), (1, -1), (-1, -1), (1, 1)]
                    directions = [(di, dj) for (di, dj) in directions if 0 <= i + di < row_len and 0 <= j + dj < col_len and matrix[i + di][j + dj] == 'A']
                    directions = [(di, dj) for (di, dj) in directions if 0 <= i + di * 2 < row_len and 0 <= j + dj * 2 < col_len and matrix[i + di * 2][j + dj * 2] == 'S']
                    if len(directions) > 0:
                        found_mas[(i, j)] = directions

                    for direction in directions:
                        direction_to_coordinate[direction].append((i, j))

        # Find all crossing MAS
        count = 0

        for ((i, j), directions) in found_mas.items():
            for direction in directions:
                if direction == (1, 1):
                    matching_coordinates = [((i + 2, j), (-1, 1)), ((i, j + 2), (1, -1))]
                elif direction == (-1, -1):
                    matching_coordinates = [((i - 2, j), (1, -1)), ((i, j - 2) ,(-1, 1))]
                elif direction == (1, -1):
                    matching_coordinates = [((i + 2, j), (-1, -1)), ((i, j - 2), (1, 1))]
                else:
                    matching_coordinates = [((i - 2, j), (1, 1)), ((i, j + 2), (-1, -1))]

                for (matching_coordinate, matching_direction) in matching_coordinates:
                    if matching_coordinate in direction_to_coordinate[matching_direction]:
                        count += 1

        return count / 2


if __name__ == '__main__':
    (Day4()).run()

