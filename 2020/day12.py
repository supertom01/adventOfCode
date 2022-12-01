from day_base import Day


class Day12(Day):

    def __init__(self):
        super().__init__(2020, 12, 'Rain Risk', expected_a=25, debug=False)

    def part_a(self) -> int:
        current_state = [0, 0, 90]  # Units north, units east, direction in degrees (north = 0)
        for instruction in self.input:
            action = instruction[0]
            value = int(instruction[1:])

            if action == "N" or (action == "F" and current_state[2] == 0):
                current_state[0] += value
            elif action == "S" or (action == "F" and current_state[2] == 180):
                current_state[0] -= value
            elif action == "E" or (action == "F" and current_state[2] == 90):
                current_state[1] += value
            elif action == "W" or (action == "F" and current_state[2] == 270):
                current_state[1] -= value
            elif action == "L":
                current_state[2] = (current_state[2] - value) % 360
            elif action == "R":
                current_state[2] = (current_state[2] + value) % 360

        # Return the Manhattan Distance
        return abs(current_state[0]) + abs(current_state[1])


if __name__ == '__main__':
    (Day12()).run()
