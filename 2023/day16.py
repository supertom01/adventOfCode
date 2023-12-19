import enum

from tqdm import tqdm

from day_base import Day


class Direction(enum.Enum):
    LEFT = 0
    RIGHT = 1
    UP = 2
    DOWN = 3

    @classmethod
    def opposite(cls, direction):
        if direction == cls.LEFT:
            return cls.RIGHT
        elif direction == cls.RIGHT:
            return cls.LEFT
        elif direction == cls.UP:
            return cls.DOWN
        elif direction == cls.DOWN:
            return cls.UP


class Day16(Day):

    def __init__(self):
        super().__init__(2023, 16, 'The Floor Will Be Lava', expected_a=46, expected_b=51, debug=True)
        self.grid = [[x for x in line] for line in self.input]
        self.width = len(self.grid[0])
        self.height = len(self.grid)

    def find_next_coordinates(self, i, j, direction):
        next_directions = []
        next_coordinate = None
        if direction == Direction.RIGHT and j + 1 < self.width:
            obj = self.grid[i][j + 1]
            next_coordinate = (i, j + 1)
            if obj == '.' or obj == '-':
                next_directions = [Direction.RIGHT]
            elif obj == '/':
                next_directions = [Direction.UP]
            elif obj == '\\':
                next_directions = [Direction.DOWN]
            elif obj == '|':
                next_directions = [Direction.UP, Direction.DOWN]
        elif direction == Direction.UP and i - 1 >= 0:
            obj = self.grid[i - 1][j]
            next_coordinate = (i - 1, j)
            if obj == '.' or obj == '|':
                next_directions = [Direction.UP]
            elif obj == '/':
                next_directions = [Direction.RIGHT]
            elif obj == '\\':
                next_directions = [Direction.LEFT]
            elif obj == '-':
                next_directions = [Direction.LEFT, Direction.RIGHT]
        elif direction == Direction.LEFT and j - 1 >= 0:
            obj = self.grid[i][j - 1]
            next_coordinate = (i, j - 1)
            if obj == '.' or obj == '-':
                next_directions = [Direction.LEFT]
            elif obj == '/':
                next_directions = [Direction.DOWN]
            elif obj == '\\':
                next_directions = [Direction.UP]
            elif obj == '|':
                next_directions = [Direction.UP, Direction.DOWN]
        elif direction == Direction.DOWN and i + 1 < self.height:
            obj = self.grid[i + 1][j]
            next_coordinate = (i + 1, j)
            if obj == '.' or obj == '|':
                next_directions = [Direction.DOWN]
            elif obj == '/':
                next_directions = [Direction.LEFT]
            elif obj == '\\':
                next_directions = [Direction.RIGHT]
            elif obj == '-':
                next_directions = [Direction.LEFT, Direction.RIGHT]

        return [(next_coordinate, next_direction) for next_direction in next_directions]

    def part_a(self):
        current_states = [((0, -1), Direction.RIGHT, 0)]
        visited_locations = []

        while len(current_states) != 0:
            updated_states = []

            for ((i, j), direction, step) in current_states:

                if ((i, j), direction) in visited_locations:
                    continue
                visited_locations.append(((i, j), direction))
                updated_states.extend(self.find_next_coordinates(i, j, direction))

            current_states = updated_states

        # Return value -1, since the starting vector does not count
        return len(set(coordinates for (coordinates, _) in visited_locations)) - 1

    def part_b(self) -> int:
        # The stupid approach, but this is still fast enough for a one time thing
        # TODO: Optimize it by checking whether longer distances are already visited if we find a coordinate with the same direction.
        #    if so, we can skip the current one
        energized_values = []
        for ((si, sj), sdirection) in tqdm([((x, -1), Direction.RIGHT) for x in range(self.height)] + [((x, self.width - 1), Direction.LEFT) for x in range(self.height)] + [((-1, y), Direction.DOWN) for y in range(self.width)] + [((self.height - 1, y), Direction.UP) for y in range(self.height)]):
            current_states = [((si, sj), sdirection)]
            visited_locations = []

            while len(current_states) != 0:
                updated_states = []

                for ((i, j), direction) in current_states:

                    if ((i, j), direction) in visited_locations:
                        continue

                    visited_locations.append(((i, j), direction))
                    updated_states.extend(self.find_next_coordinates(i, j, direction))

                current_states = updated_states

            energized_values.append(len(set(coordinates for (coordinates, _) in visited_locations)) - 1)

        # Return value -1, since the starting vector does not count
        return max(energized_values)


if __name__ == '__main__':
    (Day16()).run()

