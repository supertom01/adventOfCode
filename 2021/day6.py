from day_base import Day


class Day6(Day):

    def __init__(self):
        super().__init__(6, "Lantern fish")
        self.input = [int(v) for v in self.input[0].split(",")]

    def calc_fish(self, nr_days: int):
        fish = [0 for _ in range(9)]

        # Fill list with initial fish
        for f in self.input:
            fish[f] += 1

        # For each day add new fish and age each existing fish
        for _ in range(nr_days):
            new = fish[0]
            for i in range(8):
                fish[i] = fish[i + 1]
                if i == 6:
                    fish[i] = fish[i + 1] + new
            fish[8] = new

        # Return the total number of fish
        return sum(fish)

    def part_a(self):
        return self.calc_fish(80)

    def part_b(self):
        return self.calc_fish(256)


if __name__ == '__main__':
    Day6().run()