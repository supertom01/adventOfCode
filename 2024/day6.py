from day_base import Day


def simulate_guard(current_direction, current_loc, lab):
    """
    Simulate a guard walking from its current location in the given direction in the lab.

    Let the guard walk in the direction, till either they find an obstruction or walk out of the frame.

    :returns: The new location, the new direction, the visited locations in the direction, whether the guard left the map
    """
    exits = False
    visited_locations = set()
    i, j = current_loc
    if current_direction == '<':
        spaces_left = lab[i][:j]
        for dj in range(len(spaces_left) - 1, -1, -1):
            if spaces_left[dj] == '#':
                current_loc = (i, dj + 1)
                current_direction = '^'
                break
            else:
                visited_locations.add((i, dj, '<'))
                exits = dj == 0

    elif current_direction == '>':
        spaces_right = lab[i][j + 1:]
        for dj in range(len(spaces_right)):
            if spaces_right[dj] == '#':
                current_loc = (i, j + dj)
                current_direction = 'v'
                break
            else:
                visited_locations.add((i, j + dj + 1, '>'))
                exits = dj + 1 == len(spaces_right)

    elif current_direction == '^':
        spaces_up = [row[j] for row in lab[:i]]
        for di in range(len(spaces_up) - 1, -1, -1):
            if spaces_up[di] == '#':
                current_loc = (di + 1, j)
                current_direction = '>'
                break
            else:
                visited_locations.add((di, j, '^'))
                exits = di == 0

    elif current_direction == 'v':
        spaces_down = [row[j] for row in lab[i + 1:]]
        for di in range(len(spaces_down)):
            if spaces_down[di] == '#':
                current_loc = (i + di, j)
                current_direction = '<'
                break
            else:
                visited_locations.add((i + di + 1, j, 'v'))
                exits = di + 1 == len(spaces_down)
    return current_loc, current_direction, visited_locations, exits


class Day6(Day):

    def __init__(self):
        super().__init__(2024, 6, 'Guard Gallivant', expected_a=41, expected_b=6, debug=False)

    def parse_data(self):
        lab = [[x for x in row] for row in self.input]
        current_loc = (-1, -1)
        current_direction = ''
        for i, row in enumerate(lab):
            for j, location in enumerate(row):
                if location in ['^', '<', '>', 'v']:
                    current_loc = (i, j)
                    current_direction = location
                    break
            if current_loc[0] != -1:
                break
        return current_direction, current_loc, lab
        
    def part_a(self):
        current_direction, current_loc, lab = self.parse_data()

        visited_locations = {(current_loc[0], current_loc[1], current_direction)}
        exits = False
        while not exits:
            current_loc, current_direction, locations, exits = simulate_guard(current_direction, current_loc, lab)
            visited_locations.update(locations)

        return len(set((i, j) for (i, j, _) in visited_locations))

    def part_b(self) -> int:
        current_direction, current_loc, lab = self.parse_data()

        loop_count = 0
        possible_obstruction_locations = [(i, j) for (i, row) in enumerate(lab) for (j, location) in enumerate(row) if location == '.']
        for (i, j) in possible_obstruction_locations:
            lab[i][j] = '#'
            copy_current_location = (current_loc[0], current_loc[1])
            copy_current_direction = current_direction

            # Simulate run of guard
            visited_locations = {(current_loc[0], current_loc[1], current_direction)}
            old_length = 0
            locations = None
            exits = False
            while not exits and (old_length != len(visited_locations) or len(locations) == 0):
                old_length = len(visited_locations)
                copy_current_location, copy_current_direction, locations, exits = simulate_guard(copy_current_direction, copy_current_location, lab)
                visited_locations.update(locations)

            # Undo obstruction
            lab[i][j] = '.'

            if not exits:
                loop_count += 1

        return loop_count


if __name__ == '__main__':
    (Day6()).run()

