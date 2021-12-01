from days.day import Day


class Day1(Day):

    def __init__(self):
        super().__init__(1)

    def part_a(self):
        """
        Calculate the number of times the depth difference has increased
        :return: The number of increases in depth
        """
        depths = self.input
        counter = 0
        for i in range(len(depths) - 1):
            if depths[i] < depths[i + 1]:
                counter += 1
        return counter

    def part_b(self):
        """
        Calculate the number of times the depth difference has increased
        However, in order to improve accuracy take the depths as groups
        of size 3.
        :return: The number of increases in depth
        """
        depths = self.input
        counter = 0
        for i in range(len(depths) - 3):
            group1 = depths[i] + depths[i + 1] + depths[i + 2]
            group2 = depths[i + 1] + depths[i + 2] + depths[i + 3]
            if group1 < group2:
                counter += 1
        return counter
