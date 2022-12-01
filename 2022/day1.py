from day_base import Day


class Day1(Day):

    def __init__(self):
        super(Day1, self).__init__(2022, 1, "Calorie Counting", input_type="str", expected_a=24000, expected_b=45000, debug=True)

    def parse_input(self):
        """
        Determines the amount of calories which each elf is carrying with themselves
        :return: A list of calories, where each index is a new elf
        """
        calories = []
        current_calorie = 0
        for line in self.input:
            if line == "":
                calories.append(current_calorie)
                current_calorie = 0
            else:
                current_calorie += int(line)
        if current_calorie != 0:
            calories.append(current_calorie)
        return calories

    def part_a(self) -> int:
        """
        Determines the maximum amount of calories carried by one elf
        """
        return max(self.parse_input())

    def part_b(self) -> int:
        """
        Determines the sum of calories carried by the top 3 calorie carrying elves.
        """
        return sum(sorted(self.parse_input(), reverse=True)[:3])


if __name__ == '__main__':
    (Day1()).run()
