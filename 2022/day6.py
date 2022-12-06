from day_base import Day


class Day6(Day):

    def __init__(self):
        super().__init__(2022, 6, 'Tuning Trouble', debug=False)

    def part_a(self) -> int:
        for i in range(len(self.input[0])):
            if len(set(self.input[0][i:i+4])) == 4:
                return i + 4

    def part_b(self) -> int:
        for i in range(len(self.input[0])):
            if len(set(self.input[0][i:i+14])) == 14:
                return i + 14


if __name__ == '__main__':
    (Day6()).run()
