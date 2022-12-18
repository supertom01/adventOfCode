from heapq import heappush, heappop

from day_base import Day

dimensions = (0, 0)


class PriorityQueue:

    def __init__(self, iterable=[]):
        self.heap = []
        for value in iterable:
            heappush(self.heap, (0, value))

    def add(self, value, priority=0):
        heappush(self.heap, (priority, value))

    def pop(self):
        _, value = heappop(self.heap)
        return value

    def __len__(self):
        return len(self.heap)


def get_neighbours(i, j, i_max, j_max):
    neighbours = {(i, j + 1), (i, j - 1), (i - 1, j), (i + 1, j)}
    return list(filter(lambda x: 0 <= x[0] < i_max and 0 <= x[1] < j_max, neighbours))


def get_successors(i, j, grid):
    neighbours = get_neighbours(i, j, *dimensions)
    current_height = grid[i][j]
    successors = []
    for (k, l) in neighbours:
        if grid[k][l] - 1 <= current_height:
            successors.append((k, l))
    return successors


def get_distance(i, j, k, l):
    return abs(i - k) + abs(j - l)


def find_path(start: tuple[int, int], goal: tuple[int, int], grid) -> list[tuple[int, int]]:
    visited = set()
    origin = dict()
    distance = {start: 0}
    frontier = PriorityQueue([start])

    while frontier:
        node = frontier.pop()
        if node in visited:
            continue
        if node == goal:
            return reconstruct_path(origin, start, node)
        visited.add(node)

        for neighbour in get_successors(*node, grid):
            frontier.add(neighbour, distance[node] + 1 + get_distance(*neighbour, *goal))
            if neighbour not in distance or distance[node] + 1 < distance[neighbour]:
                distance[neighbour] = distance[node] + 1
                origin[neighbour] = node
    return None


def reconstruct_path(came_from, start, goal):
    reverse_path = [goal]
    while goal != start:
        goal = came_from[goal]
        reverse_path.append(goal)
    return list(reversed(reverse_path))


def print_grid_attempted(grid, locations):
    for i, row in enumerate(grid):
        str_row = ""
        for j, val in enumerate(row):
            if (i, j) in locations:
                str_row += "\033[92m" + chr(ord('a') + grid[i][j]) + "\033[0m"
            else:
                str_row += chr(ord('a') + val)
        print(str_row)
    print()


class Day12(Day):
    """
    With the help of A* search we find the shortest path from S to E.
    The implementation of the A* search algorithm is based on
        https://leetcode.com/problems/shortest-path-in-binary-matrix/solutions/313347/A*-search-in-Python/
    """

    def __init__(self):
        super().__init__(2022, 12, 'Hill Climbing Algorithm', expected_a=31, expected_b=29, debug=False)

    def parse(self):
        grid = [[ord(char) - ord('a') for char in row] for row in self.input]
        start_pos = None
        for i, row in enumerate(grid):
            for j, height in enumerate(row):
                if height == ord('S') - ord('a'):
                    grid[i][j] = -1
                    start_pos = (i, j)
                if height == ord('E') - ord('a'):
                    grid[i][j] = 26
                    end_pos = (i, j)
        return grid, start_pos, end_pos

    def part_a(self) -> int:
        grid, start_position, end_position = self.parse()
        global dimensions
        dimensions = (len(grid), len(grid[0]))
        path = find_path(start_position, end_position, grid)
        return len(path) - 1

    def part_b(self) -> int:
        grid, _, end_position = self.parse()
        global dimensions

        # Replace the original starting position.
        grid = [[(x if x > 0 else 0) for x in row] for row in grid]

        # Find all possible starting coordinates.
        starting_coordinates = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    starting_coordinates.append((i, j))

        # Find the shortest path
        shortest_path = None

        for i, starting_coordinate in enumerate(starting_coordinates):
            path = find_path(starting_coordinate, end_position, grid)
            if path is not None and (shortest_path is None or len(shortest_path) > len(path)):
                shortest_path = path

        return len(shortest_path) - 1


if __name__ == '__main__':
    (Day12()).run()
