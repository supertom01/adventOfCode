import re

from day_base import Day


class Day1(Day):

    def __init__(self):
        super().__init__(2023, 1, 'Trebuchet?!', expected_a=142, expected_b=281, debug=False)

    def part_a(self) -> int:
        return sum(int(re.search("[0-9]", line).group() + re.search("[0-9]", line[::-1]).group()) for line in self.input)

    def part_b(self) -> int:
        match_str = {
            "one": "1",
            "two": "2",
            "three": "3",
            "four": "4",
            "five": "5",
            "six": "6",
            "seven": "7",
            "eight": "8",
            "nine": "9",
            "ten": "10"
        }
        s = 0
        for line in self.input:
            fst = re.search("[0-9]|one|two|three|four|five|six|seven|eight|nine", line).group()
            if fst in match_str.keys():
                fst = match_str[fst]
            lst = re.search("[0-9]|eno|owt|eerht|ruof|evif|xis|neves|thgie|enin", line[::-1]).group()
            if lst[::-1] in match_str.keys():
                lst = match_str[lst[::-1]]
            s += int(fst + lst)
        return s


if __name__ == '__main__':
    (Day1()).run()