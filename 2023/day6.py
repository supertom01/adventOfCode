import math
import re
from functools import reduce

from day_base import Day


def find_ways_to_win(data):
    # One-liner
    return reduce(
        lambda x, y: x * y,
        (
            sum(
                1 if ((time - press_time) * press_time) > record_distance else 0
                for press_time in range(time + 1)
            )
            for (time, record_distance) in data
        ),
        1
    )

    # Verbose solution
    ways_to_win = []
    for (time, record_distance) in data:
        times_won = 0
        for press_time in range(time + 1):
            remaining_time = time - press_time
            travelled_distance = remaining_time * press_time
            if travelled_distance > record_distance:
                times_won += 1
        ways_to_win.append(times_won)

    return reduce(lambda x, y: x * y, ways_to_win, 1)


class Day6(Day):

    def __init__(self):
        super().__init__(2023, 6, 'Wait For It', expected_a=288, expected_b=71503, debug=False)

    def part_a(self) -> int:
        # There are multiple races, for which we both get the time and the record distance for that time.
        data = [(int(time), int(distance)) for (time, distance) in zip(
            re.split(r"\s+", re.split(r":\s+", self.input[0])[1]),
            re.split(r"\s+", re.split(r":\s+", self.input[1])[1])
        )]
        return find_ways_to_win(data)

    def part_b(self) -> int:
        # Ignore the spaces between the numbers and merge them together into a big single timeslot.
        data = [(
            int("".join(re.split(r"\s+", re.split(r":\s+", self.input[0])[1]))),
            int("".join(re.split(r"\s+", re.split(r":\s+", self.input[1])[1]))),
        )]
        return find_ways_to_win(data)


if __name__ == '__main__':
    (Day6()).run()
