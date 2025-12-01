from day_base import Day


class Day1(Day):

    def __init__(self):
        super().__init__(2025, 1, 'Secret Entrance', debug=False, expected_a=3, expected_b=6)
        
    def part_a(self):
        start = 50
        zero_visited = 0

        for line in self.input:
            direction, distance = line[0], int(line[1:])
            if direction == 'L':
                start -= distance
            elif direction == 'R':
                start += distance
            else:
                raise NotImplementedError(direction)

            start %= 100

            if start == 0:
                zero_visited += 1

        return zero_visited

    def part_b(self) -> int:
        location = 50
        zero_visited = 0

        for line in self.input:
            previous_location = location
            direction, distance = line[0], int(line[1:])

            nr_of_rotations = distance // 100

            if direction == 'L':
                location -= distance
                location += nr_of_rotations * 100
            elif direction == 'R':
                location += distance
                location -= nr_of_rotations * 100
            else:
                raise NotImplementedError(direction)

            if location > 99 or (previous_location != 0 and location <= 0):
                zero_visited += 1

            zero_visited += nr_of_rotations

            location %= 100

        return zero_visited


if __name__ == '__main__':
    (Day1()).run()

