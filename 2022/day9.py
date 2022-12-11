import enum

from day_base import Day


class Day9(Day):

    def __init__(self):
        super().__init__(2022, 9, 'Rope Bridge', expected_a=13, debug=False)

    def part_a(self) -> int:
        head = (0, 0)   # Coordinate of the head (i, j)
        tail = (0, 0)   # Coordinate of the tail (i, j)
        tail_locations = set()
        tail_locations.add(tail)

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

            for _ in range(int(distance)):
                head = (head[0] + vector[0], head[1] + vector[1])
                diff = (head[0] - tail[0], head[1] - tail[1])

                # Head and tail are separated in the same row or column
                if (abs(diff[0]) == 2 or abs(diff[1]) == 2) and abs(sum(diff)) == 2:
                    tail = (tail[0] + vector[0], tail[1] + vector[1])
                # Move the tail diagonally to the head
                elif abs(diff[0]) == 1 and abs(diff[1]) == 2 or abs(diff[0]) == 2 and abs(diff[1]) == 1:
                    tail_vector = (max(-1, min(1, diff[0])), max(-1, min(1, diff[1])))
                    tail = (tail[0] + tail_vector[0], tail[1] + tail_vector[1])
                tail_locations.add(tail)
        return len(tail_locations)


if __name__ == '__main__':
    (Day9()).run()
