from day_base import Day


def parse_index(indicators: str, min, max) -> int:
    """
    Based on the boarding pass string either the column or row is determined.
    :param indicators: A string consisting out of F's and B's or R's and L's.
    :param min: The minimum number of the indices (always 0)
    :param max: The maximum number of the indices (either 127 or 7)
    :return: The column or row index
    """
    for indicator in indicators:
        diff = ((max - min) + 1) / 2
        if indicator == 'F' or indicator == 'L':
            max -= diff
        else:
            min += diff

    assert min == max
    return min


def get_seat_id(boarding_pass: str) -> int:
    """
    Calculates the id of the seat for the given boarding pass.
    :param boarding_pass: A string with seven row indicators and three column indicators.
    :return: The seat id of this boarding pass
    """
    seat_row = parse_index(boarding_pass[0:7], 0, 127)
    seat_column = parse_index(boarding_pass[7:10], 0, 7)
    return seat_column + seat_row * 8


class Day5(Day):

    def __init__(self):
        super(Day5, self).__init__(2020, 5, "Binary Boarding")

    def part_a(self):
        """
        Finds the highest seat id
        """
        highest_id = 0
        for boarding_pass in self.input:
            seat_id = get_seat_id(boarding_pass)
            if seat_id > highest_id:
                highest_id = seat_id
        return highest_id

    def part_b(self):
        """
        Finds the sole missing seat id
        """
        ids = sorted(get_seat_id(boarding_pass) for boarding_pass in self.input)
        for i in range(1, len(ids) - 1):
            if ids[i - 1] + 2 == ids[i] and ids[i] + 1 == ids[i + 1]:
                return ids[i - 1] + 1


if __name__ == '__main__':
    (Day5()).run()