
from day_base import Day


def check_levels(used_levels):
    is_fully_increasing = True
    is_fully_decreasing = True
    step_check = True
    for j in range(len(used_levels) - 1):
        is_fully_increasing = is_fully_increasing and used_levels[j + 1] - used_levels[j] > 0
        is_fully_decreasing = is_fully_decreasing and used_levels[j + 1] - used_levels[j] < 0
        step_check = step_check and 1 <= abs(used_levels[j + 1] - used_levels[j]) <= 3
    return (is_fully_increasing or is_fully_decreasing) and step_check


class Day2(Day):

    def __init__(self):
        super().__init__(2024, 2, 'Red-Nosed Reports', expected_a=2, expected_b=4, debug=False)
        
    def part_a(self):
        nr_safe_reports = 0
        for report in self.input:
            levels = [int(x) for x in report.split(" ")]
            if check_levels(levels):
                nr_safe_reports += 1

        return nr_safe_reports

    def part_b(self) -> int:
        nr_safe_reports = 0
        for report in self.input:
            levels = [int(x) for x in report.split(" ")]

            for i in range(-1, len(levels)):
                # Naive solution, but oh well. It works.
                if i == -1:
                    used_levels = levels
                else:
                    used_levels = levels[:i] + levels[i+1:]

                if check_levels(used_levels):
                    nr_safe_reports += 1
                    break

        return nr_safe_reports


if __name__ == '__main__':
    (Day2()).run()

