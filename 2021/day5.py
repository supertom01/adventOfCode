from day_base import Day


def fill_field(field, coordinates, use_diagonal):
    for (p1, p2, is_vertical, is_horizontal, is_x_positive, is_y_positive) in coordinates:
        x = 1
        y = 1
        if not is_x_positive:
            x = -1
        if not is_y_positive:
            y = -1

        if is_horizontal:
            for i in range(abs(p1[0] - p2[0]) + 1):
                field[p1[1]][p1[0] + (x * i)] += 1
        elif is_vertical:
            for i in range(abs(p1[1] - p2[1]) + 1):
                field[p1[1] + (y * i)][p1[0]] += 1
        elif use_diagonal:
            for i in range(abs(p1[0] - p2[0]) + 1):
                field[p1[1] + (y * i)][p1[0] + (x * i)] += 1

    return field


class Day5(Day):

    def __init__(self):
        super().__init__(2021, 5, "Hydrothermal Venture", input_type="str")
        self.coordinates = [[[int(x) for x in p.split(",")] for p in line.split(" -> ")] for line in self.input]

    def add_meta_data(self):
        coordinates = []
        for [[x1, y1], [x2, y2]] in self.coordinates:
            coordinates.append(([x1, y1], [x2, y2], x1 == x2, y1 == y2, x1 < x2, y1 < y2))
        return coordinates

    def generate_field(self):
        max_x = max(max(self.coordinates, key=lambda p: p[0][0])[0][0],
                    max(self.coordinates, key=lambda p: p[1][0])[1][0])

        max_y = max(max(self.coordinates, key=lambda p: p[0][1])[0][1],
                    max(self.coordinates, key=lambda p: p[1][1])[1][0])
        return [[0 for _ in range(max_x + 1)] for _ in range(max_y + 1)]

    def part_a(self):
        field = fill_field(self.generate_field(), self.add_meta_data(), False)
        return sum(sum(1 for c in row if c > 1) for row in field)

    def part_b(self):
        field = fill_field(self.generate_field(), self.add_meta_data(), True)
        return sum(sum(1 for c in row if c > 1) for row in field)


if __name__ == '__main__':
    Day5().run()
