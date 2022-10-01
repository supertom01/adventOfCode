from day_base import Day


class Day1(Day):
    
    def __init__(self):
        super(Day1, self).__init__(2020, 1, "Report Repair", input_type="int")

    def part_a(self):
        for i in range(len(self.input)):
            for j in range(i, len(self.input)):
                if self.input[i] + self.input[j] == 2020:
                    return self.input[i] * self.input[j]

    def part_b(self):
        for i in range(len(self.input)):
            for j in range(i, len(self.input)):
                for k in range(j, len(self.input)):
                    if self.input[i] + self.input[j] + self.input[k] == 2020:
                        return self.input[i] * self.input[j] * self.input[k]


if __name__ == '__main__':
    (Day1()).run()
