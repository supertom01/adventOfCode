from day_base import Day


class Day2(Day):

    def __init__(self):
        super().__init__(2, "Dive!", input_type="str")

    def part_a(self):
        """
        A submarine can take the following commands:
            forward X -> Increases horizontal position by X
            down X -> Increases the depth by X
            up X -> Decreases the depth by X
        What do you get if you multiply your final horizontal position by your final depth?
        :return: final horizontal position * final depth
        """
        depth = 0
        horizontal_pos = 0
        for command in self.input:
            instruction = command.split(" ")[0]
            value = int(command.split(" ")[1])

            if instruction == "forward":
                horizontal_pos += value
            elif instruction == "down":
                depth += value
            elif instruction == "up":
                depth -= value
            else:
                raise ValueError(f"Unexpected instruction: {instruction}")

        return depth * horizontal_pos

    def part_b(self):
        """
        A submarine can take the following commands:
            forward X -> Increases horizontal position by X AND increases depth by (aim * X)
            down X -> Increases aim by X
            up X -> Decreases aim by X
        What do you get if you multiply your final horizontal position by your final depth?
        :return: final horizontal position * final depth
        """
        depth = 0
        horizontal_pos = 0
        aim = 0
        for command in self.input:
            instruction = command.split(" ")[0]
            value = int(command.split(" ")[1])

            if instruction == "down":
                aim += value
            elif instruction == "up":
                aim -= value
            elif instruction == "forward":
                horizontal_pos += value
                depth += aim * value
            else:
                raise ValueError(f"Unexpected instruction: {instruction}")
        return horizontal_pos * depth


if __name__ == '__main__':
    Day2().run()