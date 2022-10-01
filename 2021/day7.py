from day_base import Day


class Day7(Day):

    def __init__(self):
        super().__init__(7, "The Treachery of Whales")
        self.input = [int(x) for x in self.input[0].split(",")]

    def part_a(self):
        return min(sum(abs(x - pos) for x in self.input) for pos in range(max(self.input)))

    def part_b(self):
        return min(sum(1/2 * (abs(x - pos) ** 2 + abs(x-pos)) for x in self.input) for pos in range(max(self.input)))


if __name__ == '__main__':
    Day7().run()