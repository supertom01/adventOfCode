from days.day import Day
import numpy as np


class Day9(Day):

    def __init__(self):
        super().__init__(9, "Smoke Basin")
        self.matrix = [[(9, 0) for _ in range(len(self.input[0]) + 2)]] + \
                      [[(9, 0)] + [(int(i), -1) for i in line] + [(9, 0)] for line in self.input] + \
                      [[(9, 0) for _ in range(len(self.input[0]) + 2)]]

    def get_low_points(self):
        low_points = []
        for i in range(1, len(self.matrix) - 1):
            for j in range(1, len(self.matrix[i]) - 1):
                point = self.matrix[i][j][0]
                left = self.matrix[i - 1][j][0]
                right = self.matrix[i + 1][j][0]
                bottom = self.matrix[i][j - 1][0]
                top = self.matrix[i][j + 1][0]

                if point < left and point < right and point < bottom and point < top:
                    low_points.append((point + 1, i, j))
        return low_points

    def part_a(self):
        low_points = self.get_low_points()
        return sum(p[0] for p in low_points)

    def part_b(self):
        low_points = self.get_low_points()
        for basin_nr in range(len(low_points)):
            v, i, j = low_points[basin_nr]
            self.matrix[i][j] = (v, basin_nr + 1)

        while sum(sum(g for (v, g) in row if g == -1 and v != 9) for row in self.matrix) != 0:
            for i in range(1, len(self.matrix) - 1):
                for j in range(1, len(self.matrix[i]) - 1):
                    _, basin_nr = self.matrix[i][j]
                    if basin_nr > 0:
                        for di in [-1, 1]:
                            neighbour_value, neighbour_basin = self.matrix[i + di][j]
                            if neighbour_basin == -1 and neighbour_value != 9:
                                self.matrix[i + di][j] = (neighbour_value, basin_nr)
                        for dj in [-1, 1]:
                            neighbour_value, neighbour_basin = self.matrix[i][j + dj]
                            if neighbour_basin == -1 and neighbour_value != 9:
                                self.matrix[i][j + dj] = (neighbour_value, basin_nr)

        basin_sizes = {}
        for row in self.matrix:
            for _, basin_nr in row:
                if basin_nr == -1 or basin_nr == 0:
                    continue
                if basin_nr not in basin_sizes:
                    basin_sizes[basin_nr] = 0
                basin_sizes[basin_nr] += 1

        return np.array(sorted(basin_sizes.values(), reverse=True)[:3]).prod()


if __name__ == '__main__':
    Day9().run()
