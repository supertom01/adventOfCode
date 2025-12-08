from day_base import Day


class Day7(Day):

    def __init__(self):
        super().__init__(2025, 7, 'Laboratories', debug=False, expected_a=21, expected_b=40)
        
    def part_a(self):
        initial_location = self.input[0].index('S')
        tachyon_locations = {initial_location}
        times_split = 0

        for line in self.input[1:]:
            splitter_locations = [i for i, x in enumerate(line) if x == '^']
            next_tachyon_locations = set()

            for tachyon_location in tachyon_locations:
                if tachyon_location in splitter_locations:
                    # Split into two beams
                    next_tachyon_locations.add(tachyon_location - 1)
                    next_tachyon_locations.add(tachyon_location + 1)

                    times_split += 1
                else:
                    # Continue straight down
                    next_tachyon_locations.add(tachyon_location)

            tachyon_locations = next_tachyon_locations

        return times_split

    def part_b(self):
        initial_location = self.input[0].index('S')
        tachyon_locations = {
            initial_location: 1
        }

        for line in self.input[1:]:
            splitter_locations = [i for i, x in enumerate(line) if x == '^']
            next_tachyon_locations = dict()

            for (tachyon_location, permutation) in tachyon_locations.items():
                if tachyon_location in splitter_locations:
                    # Split into two beams
                    if tachyon_location - 1 in next_tachyon_locations.keys():
                        next_tachyon_locations[tachyon_location - 1] += permutation
                    else:
                        next_tachyon_locations[tachyon_location - 1] = permutation

                    if tachyon_location + 1 in next_tachyon_locations.keys():
                        next_tachyon_locations[tachyon_location + 1] += permutation
                    else:
                        next_tachyon_locations[tachyon_location + 1] = permutation
                else:
                    # Continue straight down
                    if tachyon_location in next_tachyon_locations.keys():
                        next_tachyon_locations[tachyon_location] += permutation
                    else:
                        next_tachyon_locations[tachyon_location] = permutation

            tachyon_locations = next_tachyon_locations

        return sum(tachyon_locations.values())

if __name__ == '__main__':
    (Day7()).run()

