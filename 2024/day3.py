import re

from day_base import Day


def evaluate_memory(memory):
    regex = re.compile(r'mul\((\d+),(\d+)\)')
    matches = re.findall(regex, memory)
    return sum(int(i1) * int(i2) for (i1, i2) in matches)


class Day3(Day):

    def __init__(self):
        super().__init__(2024, 3, 'Mull It Over', expected_a=161, expected_b=48, debug=False)

    def part_a(self):
        return evaluate_memory(''.join(self.input))

    def part_b(self) -> int:
        memory = ''.join(self.input)

        # Use the non-greedy Kleene star operator
        dont_pattern = re.compile(r"don't\(\).*?do\(\)")
        cleaned_memory = ''.join(re.split(dont_pattern, memory))

        # There might be a trailing don't
        suffix = re.match(r"don't.*", cleaned_memory)
        if suffix:
            cleaned_memory = cleaned_memory.removesuffix(suffix.group())

        return evaluate_memory(''.join(cleaned_memory))

if __name__ == '__main__':
    (Day3()).run()

