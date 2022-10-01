from day_base import Day


class Day8(Day):

    def __init__(self):
        super().__init__(8, "Seven Segment Search", debug=True)

        # Mapping #segments -> #
        self.unique_segment_count = {
            2: 1,
            4: 4,
            3: 7,
            7: 8
        }

    def part_a(self):
        count = 0
        for line in self.input:
            for signal in line.split(" | ")[1].split(" "):
                if len(signal) in self.unique_segment_count.keys():
                    count += 1
        return count


if __name__ == '__main__':
    Day8().run()
