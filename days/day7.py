from days.day import Day


class Day7(Day):

    def __init__(self):
        super().__init__(7, "The Treachery of Whales")
        self.input = [int(x) for x in self.input[0].split(",")]

    def part_a(self):
        min_fuel = max(self.input) * len(self.input)
        for pos in range(max(self.input)):
            fuel = sum(abs(x - pos) for x in self.input)
            if fuel < min_fuel:
                min_fuel = fuel
        return min_fuel

    def part_b(self):
        # Use that fuel_use = 1/2 * (n^2 + n)
        min_fuel = (1/2) * ((max(self.input) * len(self.input)) ** 2 + (max(self.input) * len(self.input)))
        for pos in range(max(self.input)):
            fuel = sum(1/2 * (abs(x - pos) ** 2 + abs(x-pos)) for x in self.input)
            if fuel < min_fuel:
                min_fuel = fuel
        return min_fuel


if __name__ == '__main__':
    Day7().run()