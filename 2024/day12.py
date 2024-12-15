from day_base import Day


def explore_region(plant_type: str, i, j, visited_locations: set[tuple[int, int]], matrix: list[list[str]], perimeter: list, area: int = 0):
    directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    for (di, dj) in directions:
        ni = di + i
        nj = dj + j
        if 0 <= ni < len(matrix) and 0 <= nj < len(matrix[0]) and matrix[ni][nj] == plant_type:
            if (ni, nj) not in visited_locations:
                visited_locations.add((ni, nj))
                area, perimeter = explore_region(plant_type, ni, nj, visited_locations, matrix, perimeter, area + 1)
        else:
            perimeter.append((ni, nj))

    return area, perimeter


class Day12(Day):

    def __init__(self):
        super().__init__(2024, 12, 'Garden Groups', debug=True, expected_a=1930, expected_b=1206)

    def part_a(self) -> int:
        matrix = [[x for x in row] for row in self.input]

        visited_locations = set()
        total_price = 0
        for i, row in enumerate(matrix):
            for j, x in enumerate(row):
                if (i, j) not in visited_locations:
                    visited_locations.add((i, j))
                    area, perimeter = explore_region(x, i, j, visited_locations, matrix, list())
                    total_price += (area + 1) * len(perimeter)
        return total_price

if __name__ == '__main__':
    (Day12()).run()

