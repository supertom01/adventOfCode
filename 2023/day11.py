from day_base import Day
import numpy as np


class Day11(Day):

    def __init__(self):
        super().__init__(2023, 11, 'Cosmic Expansion', expected_a=374, expected_b=1030, debug=False)

    def calculate_galaxy_distance(self, expanding_multiplier):
        universe = []
        galaxy_count = 0
        for line in self.input:
            row = []
            for char in line:
                if char == '#':
                    row.append(galaxy_count)
                    galaxy_count += 1
                else:
                    row.append(None)
            universe.append(row)
        universe = np.array(universe)

        # Find the locations to expand on.
        expanding_i = []
        for i, row in enumerate(universe):
            if all(x is None for x in row):
                expanding_i.append(i)

        expanding_j = []
        for j, col in enumerate(np.transpose(universe)):
            if all(x is None for x in col):
                expanding_j.append(j)

        # Find the coordinates of each universe.
        # While taking into account the expansion multiplier.
        galaxy_location = [None for _ in range(galaxy_count)]
        for i, row in enumerate(universe):
            for j, universe in enumerate(row):
                if universe is not None:
                    times_to_expand_i = len(list(filter(lambda x: x < i, expanding_i))) * (expanding_multiplier - 1)
                    times_to_expand_j = len(list(filter(lambda x: x < j, expanding_j))) * (expanding_multiplier - 1)
                    galaxy_location[universe] = (i + times_to_expand_i, j + times_to_expand_j)

        # Determine all pairs find the differences in their locations
        pairs = [[(i, j) for j in range(i + 1, galaxy_count)] for i in range(galaxy_count)]
        pairs = [item for row in pairs for item in row]
        total_distance = 0
        for (galaxy_1, galaxy_2) in pairs:
            horizontal_distance = abs(galaxy_location[galaxy_1][0] - galaxy_location[galaxy_2][0])
            vertical_distance = abs(galaxy_location[galaxy_1][1] - galaxy_location[galaxy_2][1])
            total_distance += (horizontal_distance + vertical_distance)

        return total_distance

    def part_a(self) -> int:
        return self.calculate_galaxy_distance(2)

    def part_b(self) -> int:
        return self.calculate_galaxy_distance(1000000)


if __name__ == '__main__':
    (Day11()).run()
