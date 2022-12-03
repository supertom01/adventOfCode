from day_base import Day


class Day15(Day):

    def __init__(self):
        super().__init__(2020, 15, 'Rambunctious Recitation', expected_a=436, debug=False)

    def get_spoken_number(self, nth_number):
        spoken_numbers = [int(x) for x in self.input[0].split(',')]
        for i in range(len(spoken_numbers) - 1, nth_number):
            last_number = spoken_numbers[i]
            if last_number in spoken_numbers[:-1]:
                last_turn_spoken = 1 + list(reversed(spoken_numbers[:-1])).index(last_number)
                spoken_numbers.append(last_turn_spoken)
            else:
                spoken_numbers.append(0)
        return spoken_numbers[nth_number - 1]

    def part_a(self) -> int:
        return self.get_spoken_number(2020)


if __name__ == '__main__':
    (Day15()).run()
