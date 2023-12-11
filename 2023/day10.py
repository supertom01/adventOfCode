import functools

from day_base import Day


def get_neighbours(i, j):
    return {
        "north": (i - 1, j),
        "west": (i, j - 1),
        "east": (i, j + 1),
        "south": (i + 1, j)
    }


class Day10(Day):

    def __init__(self):
        super().__init__(2023, 10, 'Pipe Maze', expected_a=80, expected_b=10, debug=False)

    def find_loop_borders(self):
        """
        Find the borders of the loop in the grid system.

        Given a starting point S, we find all the outer nodes on this loop, and keep track on how many steps it takes
        us before we have seen all the outer nodes.

        Return (steps_taken, outer_borders)
        """
        grid = [[char for char in line] for line in self.input]

        # Extend the grid, so we can safely look for neighbours.
        grid = ([['.' for _ in range(len(self.input[0]) + 2)]] +
                [['.'] + line + ['.'] for line in grid] +
                [['.' for _ in range(len(self.input[0]) + 2)]])

        # Determine the starting location
        current_location = [(0, 0), (0, 0)]
        current_values = ['S', 'S']
        for i, line in enumerate(grid):
            for j, char in enumerate(line):
                if char == 'S':
                    current_location = [(i, j), (i, j)]

        # Find all the outer nodes of this loop
        prev_locations = set()
        steps_taken = 0
        while current_location[0] != current_location[1] or current_values[0] == 'S':
            prev_locations.update(current_location)
            new_locations = current_location
            for loc_index, location in enumerate(current_location):
                neighbours = get_neighbours(*location)
                seen_neighbours = dict()
                for direction, coord in neighbours.items():
                    seen_neighbours[direction] = coord in prev_locations

                # We need to find dynamically where we can start
                if current_values[loc_index] == 'S':
                    neighbour_values = dict()
                    for direction, (i, j) in neighbours.items():
                        neighbour_values[direction] = grid[i][j]

                    # Check where we're going
                    if (neighbour_values['west'] == '-' or neighbour_values['west'] == 'F' or neighbour_values[
                        'west'] == 'L') and (loc_index == 0 or new_locations[0] != neighbours['west']):
                        new_locations[loc_index] = neighbours['west']
                    elif (neighbour_values['north'] == '|' or neighbour_values['north'] == 'F' or neighbour_values[
                        'north'] == '7') and (loc_index == 0 or new_locations[0] != neighbours['north']):
                        new_locations[loc_index] = neighbours['north']
                    elif (neighbour_values['east'] == '-' or neighbour_values['east'] == '7' or neighbour_values[
                        'east'] == 'J') and (loc_index == 0 or new_locations[0] != neighbours['east']):
                        new_locations[loc_index] = neighbours['east']
                    else:
                        new_locations[loc_index] = neighbours['south']

                # Otherwise we can simply follow our current value.
                elif current_values[loc_index] == '|':
                    # We already visited north, so go south
                    if seen_neighbours['north']:
                        new_locations[loc_index] = neighbours['south']
                    # We haven't seen north yet, so go there
                    else:
                        new_locations[loc_index] = neighbours['north']
                elif current_values[loc_index] == '-':
                    # We already visited west, so go east.
                    if seen_neighbours['west']:
                        new_locations[loc_index] = neighbours['east']
                    # We haven't seen west yet, so go there
                    else:
                        new_locations[loc_index] = neighbours['west']
                elif current_values[loc_index] == 'L':
                    if seen_neighbours['north']:
                        new_locations[loc_index] = neighbours['east']
                    else:
                        new_locations[loc_index] = neighbours['north']
                elif current_values[loc_index] == 'J':
                    if seen_neighbours['west']:
                        new_locations[loc_index] = neighbours['north']
                    else:
                        new_locations[loc_index] = neighbours['west']
                elif current_values[loc_index] == '7':
                    if seen_neighbours['west']:
                        new_locations[loc_index] = neighbours['south']
                    else:
                        new_locations[loc_index] = neighbours['west']
                elif current_values[loc_index] == 'F':
                    if seen_neighbours['east']:
                        new_locations[loc_index] = neighbours['south']
                    else:
                        new_locations[loc_index] = neighbours['east']

                current_values[loc_index] = grid[new_locations[loc_index][0]][new_locations[loc_index][1]]
            current_location = new_locations
            steps_taken += 1

        prev_locations.update(current_location)
        return steps_taken, prev_locations

    def part_a(self) -> int:
        return self.find_loop_borders()[0]

    def part_b(self) -> int:
        loop_borders_set = self.find_loop_borders()[1]
        grid = ([[0 for _ in range(len(self.input[0]) + 2)]] +
            [[0 for _ in range(len(line) + 2)] for line in self.input] +
            [[0 for _ in range(len(self.input[0]) + 2)]])

        # Set all the outer borders to 1
        for (i, j) in loop_borders_set:
            grid[i][j] = 1

        outside_nodes = [[False for _ in row] for row in grid]

        # Plants a single seed that can then grow throughout the entire system.
        # TODO: Plant seeds in all the nooks and cranks of the pipe structure.

        # Entrances from the border are visible are marked by the combinations:
        # JL 7F L  7
        #       F  J
        #
        # These are then connected by an arbitrary amount of cornering sections:
        # J    L
        #  F  7
        #
        # And straight sections:
        # ||   -
        #      -
        outside_nodes[0][0] = True
        prev_outside_nodes = None

        # Since we work from left to right and top to bottom, not all open spaces are immediately identified
        # So we keep iterating till the result stabilizes.
        while outside_nodes != prev_outside_nodes:
            prev_outside_nodes = [[x for x in xs] for xs in outside_nodes]
            height = len(outside_nodes)
            width = len(outside_nodes[0])
            for i in range(height):
                for j in range(width):
                    if outside_nodes[i][j]:
                        continue
                    if grid[i][j] == 0:
                        neighbours = list(filter(lambda x: 0 <= x[0] < height and 0 <= x[1] < width, get_neighbours(i, j).values()))
                        outside_nodes[i][j] = any(outside_nodes[n_i][n_j] for (n_i, n_j) in neighbours)

        inside_nodes = sum(sum(1 if grid[i][j] != 1 and not outside_nodes[i][j] else 0 for j in range(width)) for i in range(height))
        return inside_nodes


if __name__ == '__main__':
    (Day10()).run()
