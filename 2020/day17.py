from copy import deepcopy

from day_base import Day


# Allow for caching of neighbouring coordinates
neighbours_3d_cache = dict()
neighbours_4d_cache = dict()


def get_neighbours_3d(x: int, y: int, z: int) -> set[tuple[int, int, int]]:
    """
    Get all the neighbours in a 3d space for the given coordinate
    :return: A set with neighbouring coordinates in tuples
    """
    global neighbours_3d_cache
    if (x, y, z) in neighbours_3d_cache.keys():
        return neighbours_3d_cache[(x, y, z)]

    neighbours = set()
    for i in range(-1, 2):
        for j in range(-1, 2):
            for k in range(-1, 2):
                neighbours.add((x + i, y + j, z + k))
    neighbours_3d_cache[(x, y, z)] = neighbours - {(x, y, z)}
    return neighbours_3d_cache[(x, y, z)]


def get_neighbours_4d(x: int, y: int, z: int, w: int) -> set[tuple[int, int, int, int]]:
    """
    Get all the neighbours in a 4d space for the given coordinate
    :return: A set with neighbouring coordinates in tuples
    """
    global neighbours_4d_cache
    if (x, y, z, w) in neighbours_4d_cache:
        return neighbours_4d_cache[(x, y, z, w)]

    neighbours = set()
    for i in range(-1, 2):
        for j in range(-1, 2):
            for k in range(-1, 2):
                for l in range(-1, 2):
                    neighbours.add((x + i, y + j, z + k, w + l))
    neighbours_4d_cache[(x, y, z, w)] = neighbours - {(x, y, z, w)}
    return neighbours_4d_cache[(x, y, z, w)]


class Day17(Day):

    def __init__(self):
        super().__init__(2020, 17, 'Conway Cubes', expected_a=112, expected_b=848, debug=False)

    def part_a(self) -> int:
        active_cube_coordinates = set()

        # Initializes the cube coordinates with the initial state
        for i in range(len(self.input)):
            for j in range(len(self.input[i])):
                if self.input[i][j] == "#":
                    active_cube_coordinates.add((i, j, 0))

        # Keep track of the space to search through (x_range, y_range, z_range)
        search_space = [[-1, len(self.input) + 1], [-1, len(self.input[0]) + 1], [-1, 2]]

        # Conduct the six cycles
        for _ in range(6):
            prev_active_cubes = deepcopy(active_cube_coordinates)

            # Find all the coordinates that we should check
            coordinates = []
            for x in range(*search_space[0]):
                for y in range(*search_space[1]):
                    for z in range(*search_space[2]):
                        coordinates.append((x, y, z))

            for coordinate in coordinates:
                neighbours = get_neighbours_3d(*coordinate)
                active_neighbour_count = sum(1 for neighbour in neighbours if neighbour in prev_active_cubes)

                if coordinate in prev_active_cubes:
                    # This is an active cube
                    if active_neighbour_count not in [2, 3]:
                        active_cube_coordinates.remove(coordinate)
                elif active_neighbour_count == 3:
                    # This is an inactive cube that is allowed to be activated
                    active_cube_coordinates.add(coordinate)
                    for i in range(len(search_space)):
                        search_space[i] = [min(search_space[i][0], coordinate[i] - 2),
                                           max(search_space[i][1], coordinate[i] + 2)]

        return len(active_cube_coordinates)

    def part_b(self) -> int:
        active_cube_coordinates = set()

        # Initializes the cube coordinates with the initial state
        for i in range(len(self.input)):
            for j in range(len(self.input[i])):
                if self.input[i][j] == "#":
                    active_cube_coordinates.add((i, j, 0, 0))

        # Keep track of the search space
        search_space = [[-1, len(self.input) + 1], [-1, len(self.input[0])], [-1, 2], [-1, 2]]

        # Conduct the six cycles
        for _ in range(6):
            prev_active_cubes = deepcopy(active_cube_coordinates)

            # Find the coordinates that we should check
            coordinates = []
            for x in range(*search_space[0]):
                for y in range(*search_space[1]):
                    for z in range(*search_space[2]):
                        for w in range(*search_space[3]):
                            coordinates.append((x, y, z, w))

            for coordinate in coordinates:
                neighbours = get_neighbours_4d(*coordinate)
                active_neighbour_count = sum(1 for neighbour in neighbours if neighbour in prev_active_cubes)

                if coordinate in prev_active_cubes:
                    # This is an active cube
                    if active_neighbour_count not in [2, 3]:
                        active_cube_coordinates.remove(coordinate)
                elif active_neighbour_count == 3:
                    active_cube_coordinates.add(coordinate)
                    for i in range(4):
                        search_space[i] = [min(search_space[i][0], coordinate[i] - 2),
                                           max(search_space[i][1], coordinate[i] + 2)]

        return len(active_cube_coordinates)


if __name__ == '__main__':
    (Day17()).run()
