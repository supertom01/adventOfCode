from day_base import Day


class Day10(Day):

    def __init__(self):
        super().__init__(2024, 10, 'Hoof It', debug=False, expected_a=36, expected_b=81)

    def find_trails(self, part_a: bool):
        """
        Find the number of trails.

        :param part_a: If set to true, we only care about the unique heads that we find, if set to false keep track of
                       all the ways that we have found the heads. This is simply the difference between using a set of
                       a list for storing the trail heads.
        """

        topographic_map = [[int(x) for x in row] for row in self.input]
        height = len(topographic_map)
        width = len(topographic_map[0])
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        total_trailheads = 0
        for i, row in enumerate(topographic_map):
            for j, x in enumerate(row):

                # We are only interested in the start of a trail head
                if x != 0:
                    continue

                # Start of a trailhead
                trailheads = {(i, j)} if part_a else [(i, j)]
                for next_height in range(1, 10):
                    new_trailheads = set() if part_a else list()
                    for (ti, tj) in trailheads:
                        for (di, dj) in directions:
                            if 0 <= (ni := ti + di) < height and 0 <= (nj := tj + dj) < width and topographic_map[ni][nj] == next_height:
                                new_trailheads.add((ni, nj)) if part_a else new_trailheads.append((ni, nj))
                    trailheads = new_trailheads
                total_trailheads += len(trailheads)

        return total_trailheads
        
    def part_a(self):
        return self.find_trails(True)

    def part_b(self) -> int:
        return self.find_trails(False)

if __name__ == '__main__':
    (Day10()).run()

