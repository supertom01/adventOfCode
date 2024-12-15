import re
from functools import reduce

from day_base import Day


class Day14(Day):

    def __init__(self):
        super().__init__(2024, 14, 'Restroom Redoubt', debug=False, expected_a=12)

    def parse_data(self):
        data = []
        for line in self.input:
            start, direction = line.split(' ')
            (si, sj) = re.findall(r'-?\d+', start)
            (di, dj) = re.findall(r'-?\d+', direction)
            (si, sj) = (int(si), int(sj))
            (di, dj) = (int(di), int(dj))
            data.append(((si, sj), (di, dj)))
        return data
        
    def part_a(self):
        if self.debug:
            width = 11
            height = 7
        else:
            width = 101
            height = 103

        final_locations = []
        data = self.parse_data()
        for ((si, sj), (di, dj)) in data:
            ei = (si + di * 100) % width
            ej = (sj + dj * 100) % height
            final_locations.append((ei, ej))

        quadrant_height = height // 2
        quadrant_width = width // 2
        quadrant_count = [0, 0, 0, 0]

        for (ei, ej) in final_locations:
            if ei < quadrant_width and ej < quadrant_height:
                quadrant_count[0] += 1
            elif ei < quadrant_width and ej > quadrant_height:
                quadrant_count[2] += 1
            elif ei > quadrant_width and ej < quadrant_height:
                quadrant_count[1] += 1
            elif ei > quadrant_width and ej > quadrant_height:
                quadrant_count[3] += 1

        return reduce(lambda x, y: x * y, quadrant_count, 1)

    def part_b(self) -> int:
        width = 101
        height = 103
        data = self.parse_data()

        for x in range(25, 1000000, 103):
            print(f'{x} seconds')
            final_locations = []
            for ((si, sj), (di, dj)) in data:
                ei = (si + di * x) % width
                ej = (sj + dj * x) % height
                final_locations.append((ei, ej))

            for i in range(height):
                for j in range(width):
                    if (i, j) in final_locations:
                        print('.', end='')
                    else:
                        print(' ', end='')
                print()
            print()
            print()
            input()


if __name__ == '__main__':
    (Day14()).run()

