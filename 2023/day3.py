import re

from day_base import Day


def find_neighbours(i, j, max_i, max_j):
    """
    Find the valid neighbours for a given coordinate, for a two-dimensional matrix.

    :param i: The first coordinate
    :param j: The second coordinate
    :param max_i: The max value for the first coordinate
    :param max_j: The max value for the second coordinate
    :return: A list of valid coordinates, excluding the provided coordinate
    """
    coords = [(i - 1, j - 1), (i - 1, j), (i - 1, j + 1), (i, j - 1), (i, j + 1), (i + 1, j - 1), (i + 1, j),
              (i + 1, j + 1)]
    return list(filter(lambda x: 0 <= x[0] < max_i and 0 <= x[1] < max_j, coords))


class Day3(Day):

    def __init__(self):
        super().__init__(2023, 3, 'Gear Ratios', expected_a=4361, expected_b=467835, debug=False)

    def valid_number(self, i, j, max_i, max_j):
        valid_coords = find_neighbours(i, j, max_i, max_j)
        for (k, l) in valid_coords:
            if self.input[k][l] != '.' and not self.input[k][l].isdigit():
                return True
        return False

    def remap_matrix(self):
        # Map each coordinate to a number, if applicable
        location_number = []
        for i, line in enumerate(self.input):
            location_number.append([None for _ in range(len(line))])
            found_numbers = [(x.span(), int(x.group())) for x in re.finditer('[0-9]+', line)]
            for coord, value in found_numbers:
                for s in range(coord[0], coord[1]):
                    location_number[i][s] = value
        return location_number

    def part_a(self) -> int:
        location_number = self.remap_matrix()

        # Find the numbers that are valid and add them to the total.
        total = 0
        for i, line in enumerate(self.input):
            j = 0
            while j < len(line):
                val = location_number[i][j]
                if val is not None and self.valid_number(i, j, len(self.input), len(line)):
                    total += val

                    # We have to make sure to not count them double!!! So we skip to the end of this number in this line
                    # Find the starting position of this number
                    while location_number[i][j] == val:
                        j -= 1

                    # Skip over this number
                    j += len(str(val))

                # Increment j for the while loop
                j += 1

        return total

    def part_b(self) -> int:
        location_number = self.remap_matrix()

        total = 0
        for i, line in enumerate(self.input):
            for j, char in enumerate(line):
                # Found a gear!
                if char == '*':
                    numbers = set(filter(lambda x: x is not None, (location_number[k][l] for (k, l) in
                                                                   find_neighbours(i, j, len(self.input), len(line)))))
                    if len(numbers) == 2:
                        total += (numbers.pop() * numbers.pop())
        return total


if __name__ == '__main__':
    (Day3()).run()
