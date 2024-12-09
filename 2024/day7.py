from day_base import Day


def concatenate_digits(x, y):
    return int(f"{x}{y}")


def calculate_recursively(values: list[int], goal: int, running_total: int = 0, allow_concatenation=False):
    if len(values) == 0:
        return running_total == goal

    if running_total > goal:
        return False

    x = values[0]
    return (
            calculate_recursively(values[1:], goal, x + running_total, allow_concatenation) or
            calculate_recursively(values[1:], goal, x * running_total, allow_concatenation) or
            (allow_concatenation and calculate_recursively(values[1:], goal, concatenate_digits(running_total, x),
                                                           allow_concatenation))
    )


class Day7(Day):

    def __init__(self):
        super().__init__(2024, 7, 'Bridge Repair', debug=True, expected_a=3749, expected_b=11387)

    def part_a(self):
        equations = [tuple(equation.split(": ")) for equation in self.input]
        equations = [(int(total), list(map(int, values.split(' ')))) for total, values in equations]

        return_value = 0
        for total, values in equations:
            if calculate_recursively(values[1:], total, values[0]):
                return_value += total

        return return_value

    def part_b(self):
        equations = [tuple(equation.split(": ")) for equation in self.input]
        equations = [(int(total), list(map(int, values.split(' ')))) for total, values in equations]

        return_value = 0
        for total, values in equations:
            if calculate_recursively(values[1:], total, values[0], allow_concatenation=True):
                return_value += total

        return return_value


if __name__ == '__main__':
    (Day7()).run()
