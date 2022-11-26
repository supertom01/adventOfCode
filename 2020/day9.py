from day_base import Day


def is_valid(preamble: list[int], value: int) -> bool:
    """
    Checks if a given value can be calculated with the sum of two values within a given list
    :param preamble: The list with the values to pick from
    :param value:    The value that should be calculated
    :return: True if the value can be calculated from the given list
    """
    for i in range(len(preamble)):
        for j in range(i + 1, len(preamble)):
            if preamble[i] + preamble[j] == value:
                return True
    return False


class Day9(Day):

    def __init__(self):
        super(Day9, self).__init__(2020, 9, "Encoding Error", input_type="int", expected_a=127, expected_b=62)
        if self.debug:
            self.preamble_size = 5
        else:
            self.preamble_size = 25

    def part_a(self):
        for i in range(self.preamble_size, len(self.input)):
            number_to_check = self.input[i]
            if not is_valid(self.input[i - self.preamble_size:i], number_to_check):
                return number_to_check

    def part_b(self):
        invalid_number = self.part_a()

        # We need to check every continues list.
        # We definitely know that it won't work if sum > value.
        # Hence, restart the calculation when this has happened.
        for i in range(len(self.input)):
            j = i + 1
            while sum(self.input[i:j]) < invalid_number:
                j += 1
            if sum(self.input[i:j]) == invalid_number:
                return min(self.input[i:j]) + max(self.input[i:j])


if __name__ == '__main__':
    (Day9()).run()
