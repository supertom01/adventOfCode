from day_base import Day


def match(design: str, towels: list[str]) -> bool:
    """
    Check whether a design can be made with a set of towels.

    This uses some smart caching, avoiding pitfalls that usually happen with backtracking and such.
    """
    attempted_strings = set()
    current_strings = {design}

    while len(current_strings) > 0:
        new_strings = set()
        for pending_string in current_strings:
            sub_strings = set(pending_string.removeprefix(towel) for towel in towels)
            if any(len(sub_string) == 0 for sub_string in sub_strings):
                return True
            new_strings.update(sub_strings - attempted_strings)
        current_strings = new_strings
        attempted_strings.update(new_strings)
    return False



class Day19(Day):

    def __init__(self):
        super().__init__(2024, 19, 'Linen Layout', debug=False, expected_a=6)

    def part_a(self) -> int:
        towels = self.input[0].split(', ')
        designs = self.input[2:]

        matches = 0
        for design in designs:
            if match(design, towels):
                matches += 1
        return matches



if __name__ == '__main__':
    (Day19()).run()

