from day_base import Day


class Day8(Day):

    def __init__(self):
        super().__init__(
            2024, 8, "Resonant Collinearity", debug=False, expected_a=14, expected_b=34
        )

    def parse_data(self):
        antennas = {}
        for i, row in enumerate(self.input):
            for j, frequency in enumerate(row):
                if frequency != ".":
                    if frequency not in antennas:
                        antennas[frequency] = []
                    antennas[frequency].append((i, j))
        return antennas

    def part_a(self):
        antennas = self.parse_data()
        antinodes = set()
        for frequency, coordinates in antennas.items():
            for k, (i1, j1) in enumerate(coordinates):
                for i2, j2 in coordinates[k + 1 :]:
                    di, dj = i2 - i1, j2 - j1
                    antinodes.update([(i1 - di, j1 - dj), (i2 + di, j2 + dj)])

        width = len(self.input[0])
        height = len(self.input)

        return len(
            [(i, j) for (i, j) in antinodes if 0 <= i < height and 0 <= j < width]
        )

    def part_b(self):
        antennas = self.parse_data()
        width = len(self.input[0])
        height = len(self.input)

        antinodes = set()
        for frequency, coordinates in antennas.items():
            for k, (i1, j1) in enumerate(coordinates):
                if len(coordinates) > 1:
                    antinodes.add((i1, j1))
                for i2, j2 in coordinates[k + 1 :]:
                    di, dj = i2 - i1, j2 - j1

                    new_i = i1
                    new_j = j1
                    while (
                        0 <= (new_i := new_i - di) < height
                        and 0 <= (new_j := new_j - dj) < width
                    ):
                        antinodes.add((new_i, new_j))

                    new_i = i2
                    new_j = j2
                    while (
                        0 <= (new_i := new_i + di) < height
                        and 0 <= (new_j := new_j + dj) < width
                    ):
                        antinodes.add((new_i, new_j))
        return len(antinodes)


if __name__ == "__main__":
    (Day8()).run()