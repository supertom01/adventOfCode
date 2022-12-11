import enum

from day_base import Day


class Day9(Day):

    def __init__(self):
        super().__init__(2022, 9, 'Rope Bridge', expected_a=None, expected_b=36, debug=False)

    def parse(self):
        instructions = []
        for instruction in self.input:
            direction, distance = instruction.split(" ")
            if direction == "R":
                vector = (0, 1)
            elif direction == "L":
                vector = (0, -1)
            elif direction == "D":
                vector = (1, 0)
            else:
                vector = (-1, 0)
            instructions.append((vector, int(distance)))
        return instructions

    def part_a(self) -> int:
        head = (0, 0)   # Coordinate of the head (i, j)
        tail = (0, 0)   # Coordinate of the tail (i, j)
        tail_locations = set()
        tail_locations.add(tail)

        for vector, distance in self.parse():
            for _ in range(distance):
                head = (head[0] + vector[0], head[1] + vector[1])
                diff = (head[0] - tail[0], head[1] - tail[1])
                tail_vector = (max(-1, min(1, diff[0])), max(-1, min(1, diff[1])))

                # Head and tail are separated in the same row or column
                if (abs(diff[0]) == 2 or abs(diff[1]) == 2) and abs(sum(diff)) == 2:
                    tail = (tail[0] + tail_vector[0], tail[1] + tail_vector[1])
                # Move the tail diagonally to the head
                elif abs(diff[0]) == 1 and abs(diff[1]) == 2 or abs(diff[0]) == 2 and abs(diff[1]) == 1:
                    tail = (tail[0] + tail_vector[0], tail[1] + tail_vector[1])
                tail_locations.add(tail)
        return len(tail_locations)

    def part_b(self) -> int:
        head = (0, 0)
        knots = [(0, 0) for _ in range(9)] # The locations of all the knots at this moment
        tail_locations = set()
        tail_locations.add(knots[8])

        for vector, distance in self.parse():
            for _ in range(distance):
                head = (head[0] + vector[0], head[1] + vector[1])

                # Determine the location for each knot
                for i in range(len(knots)):
                    knot = knots[i]
                    previous_knot = head if i == 0 else knots[i - 1]
                    diff = (previous_knot[0] - knot[0], previous_knot[1] - knot[1])
                    knot_vector = (max(-1, min(1, diff[0])), max(-1, min(1, diff[1])))

                    # Previous knot and this knot are separated in the same row or column
                    if (abs(diff[0]) == 2 or abs(diff[1]) == 2) and abs(sum(diff)) == 2 or abs(diff[0]) + abs(diff[1]) > 2:
                        knot = (knot[0] + knot_vector[0], knot[1] + knot_vector[1])
                    knots[i] = knot

                    if i == 8:
                        tail_locations.add(knot)
        return len(tail_locations)


if __name__ == '__main__':
    (Day9()).run()
