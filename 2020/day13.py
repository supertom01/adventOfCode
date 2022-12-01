import math
import operator

from day_base import Day


class Day13(Day):

    def __init__(self):
        super().__init__(2020, 13, 'Shuttle Search', expected_a=295, expected_b=1068781, debug=False)

    def part_a(self) -> int:
        timestamp = int(self.input[0])
        busses = [int(x) for x in self.input[1].split(',') if x != 'x']

        time_left = [(bus_nr, bus_nr - timestamp % bus_nr) for bus_nr in busses]
        min_wait = min(time_left, key=lambda x: x[1])
        return min_wait[0] * min_wait[1]

    def part_b(self) -> int:
        split_busses = self.input[1].split(',')

        # Create a list with (bus_nr, offset)
        busses = []
        for i in range(len(split_busses)):
            if split_busses[i] != 'x':
                busses.append((int(split_busses[i]), i))

        # Find max step size
        max_id, offset_max_id = max(busses, key=lambda x: x[0])

        # Lets go and validate!
        done = False
        timestamp = max_id - offset_max_id  # The timestamp at which the first bus should arrive
        in_order = 0                        # The amount of busses that have arrived at the correct offset till this moment
        step_size = max_id                  # The step size that we will be taking in each tick
        while not done:
            current_round_in_order = 0
            nrs_in_order = set()
            done = True
            timestamp += step_size

            for bus_nr, offset in busses:
                if (timestamp + offset) % bus_nr == 0:
                    # A bus arrived at its supposed offset!
                    current_round_in_order += 1
                    nrs_in_order.add(bus_nr)
                else:
                    done = False

            # Check if already more busses are arriving in order.
            # If that is the case, we will update the step size, to make sure that this keeps happening
            if current_round_in_order > in_order:
                in_order = current_round_in_order
                nrs_in_order.add(1)
                step_size = math.prod(nrs_in_order)
        return timestamp


if __name__ == '__main__':
    (Day13()).run()
