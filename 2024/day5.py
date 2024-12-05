import functools

from day_base import Day


def fix_updates(updates, rules):
    comparator = functools.cmp_to_key(lambda a, b: -1 if (a, b) in rules else (1 if (b, a) in rules else 0))
    correct_updates = []
    corrected_updates = []
    for update in updates:
        corrected_update = sorted(update, key=comparator)
        if update == corrected_update:
            correct_updates.append(update)
        else:
            corrected_updates.append(corrected_update)
    return correct_updates, corrected_updates


class Day5(Day):

    def __init__(self):
        super().__init__(2024, 5, 'Print Queue', expected_a=143, expected_b=123, debug=False)

    def parse_data(self):
        rules: list[tuple[int, int]] = []
        updates: list[list[int]] = []
        for line in self.input:
            if '|' in line:
                l, r = line.split('|')
                rules.append((int(l), int(r)))
            elif len(line) != 0:
                updates.append([int(x) for x in line.split(',')])
        return updates, rules

    def part_a(self):
        updates, rules = self.parse_data()
        correct_updates, _ = fix_updates(updates, rules)

        return sum(x[int(len(x) / 2)] for x in correct_updates)

    def part_b(self) -> int:
        updates, rules = self.parse_data()
        _, corrected_updates = fix_updates(updates, rules)
        return sum(x[int(len(x) / 2)] for x in corrected_updates)

if __name__ == '__main__':
    (Day5()).run()

