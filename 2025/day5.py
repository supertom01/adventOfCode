
from day_base import Day


class Day5(Day):

    def __init__(self):
        super().__init__(2025, 5, 'Cafeteria', debug=False, expected_a=3, expected_b=14)
        
    def part_a(self):
        fresh_ingredients = list()
        available_ingredient_count = 0
        reading_ranges = True

        for line in self.input:

            if line.strip() == '':
                reading_ranges = False

            elif reading_ranges:
                start, stop = line.split('-')
                fresh_ingredients.append((int(start), int(stop)))

            else:
                for start, stop in fresh_ingredients:
                    if start <= int(line) <= stop:
                        available_ingredient_count += 1
                        break

        return available_ingredient_count

    def part_b(self) -> int:
        fresh_ranges = list()

        for line in self.input:
            if line.strip() == '':
                break

            start, stop = line.split('-')
            fresh_ranges.append((int(start), int(stop)))

        fresh_ranges = sorted(fresh_ranges, key=lambda x: x[0])
        i = 0

        while i < len(fresh_ranges) - 1:
            start, stop = fresh_ranges[i]
            next_start, next_stop = fresh_ranges[i + 1]

            if next_start <= stop:
                fresh_ranges[i] = (start, max(stop, next_stop))
                fresh_ranges.remove((next_start, next_stop))
            else:
                i += 1

        fresh_ingredients = 0
        for start, stop in fresh_ranges:
            fresh_ingredients += (stop - start) + 1

        return fresh_ingredients


if __name__ == '__main__':
    (Day5()).run()

