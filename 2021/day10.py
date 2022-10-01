import math

from day_base import Day


class Day10(Day):

    def __init__(self):
        super().__init__(2021, 10, "Syntax Scoring")
        self.closing_open = {
            ')': '(',
            ']': '[',
            '}': '{',
            '>': '<'
        }

    def part_a(self):
        point_map = {
            ')': 3,
            ']': 57,
            '}': 1197,
            '>': 25137
        }

        points = 0
        for line in self.input:
            bracket_scopes = []
            for item in line:
                if item in self.closing_open.values():
                    bracket_scopes.append(item)
                elif self.closing_open[item] == bracket_scopes[len(bracket_scopes) - 1][0]:
                    bracket_scopes.pop()
                else:
                    # Corrupt line
                    points += point_map[item]
                    break
        return points

    def part_b(self):
        point_map = {
            '(': 1,
            '[': 2,
            '{': 3,
            '<': 4
        }

        # Filter out the corrupt lines
        corrupt_lines = []
        for l in self.input:
            scopes = []
            for i in l:
                if i in self.closing_open.values():
                    scopes.append(i)
                elif self.closing_open[i] == scopes[len(scopes) - 1]:
                    scopes.pop()
                else:
                    corrupt_lines.append(l)
                    break
        incomplete_lines = list(set(self.input) - set(corrupt_lines))

        # Calculate the points!
        all_points = []
        for l in incomplete_lines:
            points = 0
            scopes = []
            for i in l:
                if i in self.closing_open.values():
                    scopes.append(i)
                else:
                    scopes.pop()
            for v in reversed(scopes):
                points = points * 5 + point_map[v]
            all_points.append(points)

        all_points = sorted(all_points)
        return all_points[math.floor(len(all_points) / 2)]


if __name__ == '__main__':
    Day10().run()