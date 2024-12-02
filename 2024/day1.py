from day_base import Day


class Day1(Day):
    
    def __init__(self):
        super().__init__(2024, 1, 'Historian Hysteria', expected_a=11, expected_b=31, debug=True)

    def part_a(self) -> int:
        left, right = list(zip(*[map(int, line.split("   ")) for line in self.input]))
        return sum(abs(l - r) for (l, r) in zip(sorted(left), sorted(right)))

    def part_b(self) -> int:
        left, right = list(zip(*[map(int, line.split("   ")) for line in self.input]))
        return sum(right.count(l) * l for l in left)

if __name__ == '__main__':
    (Day1()).run()