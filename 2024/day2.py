
from day_base import Day


def check_levels(used_levels):
    difference = [l1 - l2 for (l1, l2) in zip(used_levels, used_levels[1:])]
    is_fully_increasing = all([1 <= x <= 3 for x in difference])
    is_fully_decreasing = all([-3 <= x <= -1 for x in difference])
    return is_fully_increasing or is_fully_decreasing


class Day2(Day):

    def __init__(self):
        super().__init__(2024, 2, 'Red-Nosed Reports', expected_a=2, expected_b=4, debug=False)
        
    def part_a(self):
        return sum(1 for report in self.input if check_levels(list(map(int, report.split(" ")))))

    def part_b(self) -> int:
        return sum(1 for r in map(lambda r: [int(x) for x in r.split(" ")], self.input) if any(check_levels(dr) for dr in [(r if i == -1 else [*r[:i], *r[i+1:]]) for i in range(-1, len(r))]))


if __name__ == '__main__':
    (Day2()).run()

