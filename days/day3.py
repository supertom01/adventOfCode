from days.day import Day


class Day3(Day):

    def __init__(self):
        super().__init__(3, "Binary Diagnostic", "str")

    def part_a(self):
        """
        The input is a list of binary numbers.
        The gamma value is determined by the most common bit along each bit index.
        The epsilon value is determined by the least common bit along each bit index.
        :return: gamma * epsilon
        """
        numbers = [[int(x) for x in number] for number in self.input]
        gamma = [int(val > (len(numbers) / 2)) for val in [sum(x[i] for x in numbers) for i in range(len(numbers[0]))]]
        epsilon = [int(not bool(x)) for x in gamma]
        return int("".join(map(str, gamma)), 2) * int("".join(map(str, epsilon)), 2)

    def part_b(self):
        oxygen_rating_list = []
        co2_rating_list = []
        for nr in self.input:
            oxygen_rating_list.append([int(c) for c in nr])
            co2_rating_list.append([int(c) for c in nr])

        i = 0
        while len(oxygen_rating_list) > 1:
            test = sum([x[i] for x in oxygen_rating_list])
            if test > len(oxygen_rating_list) / 2 or test == len(oxygen_rating_list) / 2:
                # 1 is the dominant bit
                oxygen_rating_list = list(filter(lambda b: b[i] == 1, oxygen_rating_list))
            else:
                # 0 is the dominant bit
                oxygen_rating_list = list(filter(lambda b: b[i] == 0, oxygen_rating_list))
            i += 1

        i = 0
        while len(co2_rating_list) > 1:
            test = sum([x[i] for x in co2_rating_list])
            if test < len(co2_rating_list) / 2:
                # 1 is the least common bit
                co2_rating_list = list(filter(lambda b: b[i] == 1, co2_rating_list))
            else:
                # 0 is the least common bit
                co2_rating_list = list(filter(lambda b: b[i] == 0, co2_rating_list))
            i += 1

        oxygen_rating_list = oxygen_rating_list[0]
        co2_rating_list = co2_rating_list[0]

        oxygen_rating = sum([x * 2**(len(oxygen_rating_list) - i - 1) for i, x in enumerate(oxygen_rating_list)])
        co2_rating = sum([x * 2**(len(co2_rating_list) - i - 1) for i, x in enumerate(co2_rating_list)])

        return oxygen_rating * co2_rating


if __name__ == '__main__':
    Day3().run()