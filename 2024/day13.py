import re
import sympy as sym

from day_base import Day


def calculate_tokens_spent(machines):
    """
    The set of buttons generates a system of linear equations that can be algebraically solved.

    Numpy however only returns a single answer, so we needed a symbolic solver.
    """
    tokens_spent = 0
    for (x1, y1), (x2, y2), (r1, r2) in machines:
        # Setup the system of equations
        a, b = sym.symbols('a,b')
        eq1 = sym.Eq(x1 * a + x2 * b, r1)
        eq2 = sym.Eq(y1 * a + y2 * b, r2)

        # Solve the system
        result: list = sym.solve([eq1, eq2], (a, b), dict=True)

        # Filter out all the numbers that are not integers
        result = [d for d in result if d[a].is_Integer and d[b].is_Integer]

        if len(result) > 0:
            # Find the cheapest combination of button presses
            d = min(result, key=lambda z: z[a] * 3 + z[b])
            a_value = int(d[a].p / d[a].q)
            b_value = int(d[b].p / d[b].q)
            tokens_spent += a_value * 3 + b_value
    return tokens_spent


class Day13(Day):

    def __init__(self):
        super().__init__(2024, 13, 'Claw Contraption', debug=False, expected_a=480)

    def parse_data(self, is_part_a: bool):
        machines = []
        regex_a = re.compile(r'Button A: X\+(?P<x>\d+), Y\+(?P<y>\d+)')
        regex_b = re.compile(r'Button B: X\+(?P<x>\d+), Y\+(?P<y>\d+)')
        regex_prize = re.compile(r'Prize: X=(?P<x>\d+), Y=(?P<y>\d+)')
        machine = []
        for i, line in enumerate(self.input):
            if (match := re.match(regex_a, line)) is not None or (match := re.match(regex_b, line)) is not None:
                x = int(match.groupdict()['x'])
                y = int(match.groupdict()['y'])
                machine.append((x, y))
            elif (match := re.match(regex_prize, line)) is not None:
                x = int(match.groupdict()['x']) + (10000000000000 if not is_part_a else 0)
                y = int(match.groupdict()['y']) + (10000000000000 if not is_part_a else 0)
                machine.append((x, y))
            if len(line) == 0:
                machines.append(machine)
                machine = []

        if len(machine) != 0:
            machines.append(machine)

        return machines

    def part_a(self):
        machines = self.parse_data(True)
        tokens_spent = calculate_tokens_spent(machines)
        return tokens_spent

    def part_b(self) -> int:
        machines = self.parse_data(False)
        tokens_spent = calculate_tokens_spent(machines)
        return tokens_spent


if __name__ == '__main__':
    (Day13()).run()

