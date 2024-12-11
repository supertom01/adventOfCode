import math

from day_base import Day


class Day11(Day):

    def __init__(self):
        super().__init__(2024, 11, 'Plutonian Pebbles', debug=False, expected_a=55312)

    def simulate_blinking(self, blinking_times: int):
        pebbles = dict((int(v), 1) for v in self.input[0].split(' '))

        for _ in range(blinking_times):
            new_pebbles = dict()
            for (pebble, count) in pebbles.items():
                new_pebble = []
                new_count = count
                if pebble == 0:
                    new_pebble.append(1)
                # If a number has an even amount of digits
                elif (pebble_size := math.floor(math.log10(pebble)) + 1) % 2 == 0:
                    digit_length = int(pebble_size / 2)
                    left = pebble // 10 ** int((math.log10(pebble) - digit_length + 1))
                    right = pebble % (10 ** digit_length)
                    new_pebble = [left, right]
                else:
                    new_pebble.append(pebble * 2024)

                for np in new_pebble:
                    if np not in new_pebbles:
                        new_pebbles[np] = 0
                    new_pebbles[np] += new_count
            pebbles = new_pebbles

        return sum(v for v in pebbles.values())
        
    def part_a(self):
        return self.simulate_blinking(25)

    def part_b(self) -> int:
        return self.simulate_blinking(75)

if __name__ == '__main__':
    (Day11()).run()

