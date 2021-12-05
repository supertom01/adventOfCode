from days.day import Day
import numpy as np


class Day5(Day):

    def __init__(self):
        super().__init__(5, "Hydrothermal Venture", input_type="str")
        self.coordinates = [[[int(x) for x in p.split(",")] for p in line.split(" -> ")] for line in self.input]

    def part_a(self):

        # (p1, p2, is_vertical, div(p1,p2) > 0)
        used_coords = []
        for [[x1, y1], [x2, y2]] in self.coordinates:
            if x1 == x2:
                used_coords.append(([x1, y1], [x2, y2], False, y1 < y2))
            elif y1 == y2:
                used_coords.append(([x1, y1], [x2, y2], True, x1 < x2))

        max_x = max(max(used_coords, key=lambda p: p[0][0])[0][0], max(used_coords, key=lambda p: p[1][0])[1][0])
        max_y = max(max(used_coords, key=lambda p: p[0][1])[0][1], max(used_coords, key=lambda p: p[1][1])[1][0])

        field = [[0 for _ in range(max_x + 1)] for _ in range(max_y + 1)]

        for (p1, p2, is_vertical, is_positive) in used_coords:
            j = 1
            if not is_positive:
                j = -1

            if is_vertical:
                for i in range(abs(p1[0] - p2[0]) + 1):
                    field[p1[1]][p1[0] + (j * i)] += 1
            else:
                for i in range(abs(p1[1] - p2[1]) + 1):
                    field[p1[1] + (j * i)][p1[0]] += 1

        return sum(sum(1 for c in row if c > 1) for row in field)

    def part_b(self):
        # (p1, p2, is_vertical, div(p1,p2) > 0)
        used_coords = []
        for [[x1, y1], [x2, y2]] in self.coordinates:
            used_coords.append(([x1, y1], [x2, y2], x1 == x2, y1 == y2, x1 < x2, y1 < y2))

        max_x = max(max(used_coords, key=lambda p: p[0][0])[0][0], max(used_coords, key=lambda p: p[1][0])[1][0])
        max_y = max(max(used_coords, key=lambda p: p[0][1])[0][1], max(used_coords, key=lambda p: p[1][1])[1][0])

        field = [[0 for _ in range(max_x + 1)] for _ in range(max_y + 1)]

        for (p1, p2, is_horizontal, is_vertical, is_x_positive, is_y_positive) in used_coords:
            x = 1
            y = 1
            if not is_x_positive:
                x = -1
            if not is_y_positive:
                y = -1

            if is_vertical:
                for i in range(abs(p1[0] - p2[0]) + 1):
                    field[p1[1]][p1[0] + (x * i)] += 1
            elif is_horizontal:
                for i in range(abs(p1[1] - p2[1]) + 1):
                    field[p1[1] + (y * i)][p1[0]] += 1
            else:
                for i in range(abs(p1[0] - p2[0]) + 1):
                    field[p1[1] + (y * i)][p1[0] + (x * i)] += 1

        return sum(sum(1 for c in row if c > 1) for row in field)


if __name__ == '__main__':
    Day5().run()
