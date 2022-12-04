from day_base import Day


class Day4(Day):

    def __init__(self):
        super().__init__(2022, 4, 'Camp Cleanup', expected_a=2, expected_b=4, debug=False)

    def parse_sections(self):
        sections = []
        for pair in self.input:
            ranges = []
            for elf in pair.split(","):
                start, end = map(int, elf.split("-"))
                ranges.append(set(range(start, end + 1)))
            sections.append(ranges)
        return sections

    def part_a(self) -> int:
        sections = self.parse_sections()
        complete_overlap_count = 0
        for group in sections:
            union = group[0].union(group[1])
            if len(union) == len(group[0]) or len(union) == len(group[1]):
                complete_overlap_count += 1
        return complete_overlap_count

    def part_b(self) -> int:
        sections = self.parse_sections()
        overlap_count = 0
        for group in sections:
            if len(group[0] & group[1]) != 0:
                overlap_count += 1
        return overlap_count

if __name__ == "__main__":
    (Day4()).run()
