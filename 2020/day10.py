import numpy as np

from day_base import Day


class Day10(Day):

    def __init__(self):
        super(Day10, self).__init__(2020, 10, "Adapter Array", input_type="int", expected_a=220, expected_b=19208, debug=False)

    def part_a(self):
        device_max_jolts = max(self.input) + 3
        jolts_available = self.input + [0, device_max_jolts]

        # Calculate the difference between each adapter
        jolt_diff = np.diff(sorted(jolts_available))

        # Figure out how often there is a 1 and 3 jolt difference
        jolt_1 = len(list(filter(lambda x: x == 1, jolt_diff)))
        jolt_3 = len(list(filter(lambda x: x == 3, jolt_diff)))
        return jolt_1 * jolt_3

    def part_b(self):
        device_max_jolts = max(self.input) + 3
        jolts_available = self.input + [0, device_max_jolts]

        # Calculate the difference between each adapter
        jolt_diff = np.diff(sorted(jolts_available))

        # Count the amount of continues streams of 1 differences
        count = 0
        groups = []
        for i in range(0, len(jolt_diff) - 1):
            if jolt_diff[i] == 1 and jolt_diff[i + 1] == 1:
                count += 1
            else:
                if count > 0:
                    groups.append(count + 1)
                count = 0

        # Determine for each group of 1s the amount of options.
        # The relation is amount of options for group_size - 1 + diff(group_size, group_size - 1)
        options = 1
        options_for_group = {1: 1}
        for group in groups:
            if group not in options_for_group.keys():
                max_known = max(options_for_group.keys())
                while max_known < group:
                    max_known += 1
                    options_for_group[max_known] = options_for_group[max_known - 1] + (max_known - 1)
            options *= options_for_group[group]
        return options


if __name__ == '__main__':
    (Day10()).run()