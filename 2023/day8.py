import math

from day_base import Day


class Day8(Day):

    def __init__(self):
        super().__init__(2023, 8, 'Haunted Wasteland', expected_a=6, expected_b=6, debug=False)

    def find_path(self, part_a: bool):
        """
        Find the required amount of steps to reach our end path.

        :param part_a If set to true, we only want the AAA node as a starting node, otherwise we want all the nodes that
                      end with an A as starting nodes.
        """
        instructions = self.input[0]
        directions = dict()
        current_nodes = []
        for line in self.input[2::]:
            source, options = line.split(" = ")
            left, right = options[1::][::-1][1::][::-1].split(", ")
            directions[source] = (left, right)

            # Collect all starting nodes.
            if (part_a and source == 'AAA') or (not part_a and source[2] == 'A'):
                current_nodes.append(source)

        steps = 0
        seen_z_at = [-1 for _ in range(len(current_nodes))]

        # While not all the nodes have seen z yet, we keep looking.
        while any(x == -1 for x in seen_z_at):
            for instruction in instructions:
                steps += 1
                if instruction == 'L':
                    current_nodes = list(map(lambda n: directions[n][0], current_nodes))
                else:
                    current_nodes = list(map(lambda n: directions[n][1], current_nodes))

                for i, node in enumerate(current_nodes):
                    if node[2] == 'Z' and seen_z_at[i] == -1:
                        seen_z_at[i] = steps

        # Since all the nodes have seen z now at least once, we know that this is a repeating pattern,
        # which can be easily resolved by taking the common multiple of the required steps to reach each node.
        return math.lcm(*seen_z_at)

    def part_a(self) -> int:
        return self.find_path(part_a=True)

    def part_b(self) -> int:
        return self.find_path(part_a=False)


if __name__ == '__main__':
    (Day8()).run()
