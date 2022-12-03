from day_base import Day


class Day15(Day):

    def __init__(self):
        super().__init__(2020, 15, 'Rambunctious Recitation', expected_a=436, expected_b=175594, debug=False)

    def get_spoken_number(self, nth_number):
        spoken_numbers = [int(x) for x in self.input[0].split(',')]
        spoken_numbers_map = dict()
        for i, nr in enumerate(spoken_numbers[:-1]):
            spoken_numbers_map[nr] = [i]

        for i in range(len(spoken_numbers) - 1, nth_number):
            last_number = spoken_numbers[i]
            if last_number in spoken_numbers_map.keys():
                last_turn_spoken = spoken_numbers_map[last_number][-1]
                spoken_numbers.append(i - last_turn_spoken)
            else:
                spoken_numbers.append(0)

            if last_number not in spoken_numbers_map:
                spoken_numbers_map[last_number] = []
            spoken_numbers_map[last_number].append(i)
        return spoken_numbers[nth_number - 1]

    def part_a(self) -> int:
        return self.get_spoken_number(2020)

    def part_b(self) -> int:
        return self.get_spoken_number(30000000)


if __name__ == '__main__':
    (Day15()).run()
