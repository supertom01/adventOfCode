import math
import re
from functools import reduce

from day_base import Day


class Day5(Day):

    def __init__(self):
        super().__init__(2023, 5, 'If You Give A Seed A Fertilizer', expected_a=35, expected_b=46, debug=False)

    def parse_input(self, part_a):
        data = {
            "seeds": list(map(int, self.input[0].split(": ")[1].split(" "))),
            "ranges": []
        }
        if not part_a:
            seed_ranges = []
            for i in range(0, len(data['seeds']), 2):
                seed_ranges.append((data['seeds'][i], data['seeds'][i + 1]))
            data['seeds'] = seed_ranges

        ranges = []
        for line in self.input[3::]:
            if line.strip() == '':
                continue
            elif 'map' in line:
                data["ranges"].append(ranges)
                ranges = []
            else:
                ranges.append(tuple(map(int, line.split(" "))))

        if len(ranges) > 0:
            data["ranges"].append(ranges)
        return data

    def part_a(self) -> int:
        data = self.parse_input(part_a=True)
        minimal_location = None

        for seed in data['seeds']:
            current_nr = seed
            for map in data['ranges']:
                for (dest, origin, r) in map:
                    if origin <= current_nr < origin + r:
                        current_nr = dest + (current_nr - origin)

                        # Matched so break out of the most inner for-loop
                        break
            if minimal_location is None or minimal_location > current_nr:
                minimal_location = current_nr

        return minimal_location

    def part_b(self) -> int:
        """
        We work in seed ranges and try to match a range of seeds to a map.
        There are three cases when we can (partially) match with a mapping.
        1. The seed range is a complete subset of the map, in that case we update the entire range in one go.
        2. The seed range only matches at the end of the map, in that case we split the seed range into two parts:
           the mapped and unmapped ranges. We store the unmapped range, such that it can be mapped again in a later stage.
        3. The seed range only matches at the beginning of the map, we again split the matched and unmatched ranges.
        """
        data = self.parse_input(part_a=False)

        seed_ranges_to_check = data['seeds']
        for map in data['ranges']:
            mapped_ranges = []
            seeds_to_map = seed_ranges_to_check
            while len(seeds_to_map) > 0:
                seeds = seeds_to_map
                seeds_to_map = []
                for (start_seed, seed_length) in seeds:
                    mapped = False
                    for (dest, origin, r) in map:

                        # We match an exact subset of the mapping range!
                        if origin <= start_seed and start_seed + seed_length < (origin + r):
                            mapped_ranges.append((dest + start_seed - origin, seed_length))
                            mapped = True

                        # Partially matched at the front of the mapping range.
                        elif origin <= start_seed < origin + r:

                            # We store the head of the range that can be mapped.
                            mapped_ranges.append((dest + (start_seed - origin), (origin + r - start_seed)))

                            # Keep searching mappings for the other parts of the seeds.
                            unmapped_tail = (origin + r, seed_length - (origin + r - start_seed))
                            seeds_to_map.append(unmapped_tail)
                            mapped = True

                        # Partially mapped at the back of the mapping range.
                        elif origin < (start_seed + seed_length) < origin + r:

                            mapped_ranges.append((dest, start_seed + seed_length - origin))
                            unmapped_head = (start_seed, origin - start_seed)
                            seeds_to_map.append(unmapped_head)
                            mapped = True

                        if mapped:
                            break

                    if not mapped:
                        # No mapping was found, then we preserve the original values.
                        mapped_ranges.append((start_seed, seed_length))
            seed_ranges_to_check = mapped_ranges

        # Return the minimal location
        return min(seed_ranges_to_check, key=lambda x: x[0])[0]


if __name__ == '__main__':
    (Day5()).run()
