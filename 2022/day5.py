from day_base import Day


class Day5(Day):

    def __init__(self):
        super().__init__(2022, 5, 'Supply Stacks', expected_a="CMZ", expected_b="MCD", debug=False)

    def parse_input(self):
        i = 0
        stacks = []
        instructions = []

        # Parse the stacks
        while self.input[i] != "":
            i += 1
        stack_string = list(reversed(self.input[0:i]))
        column_index = [i for i in range(len(stack_string[0])) if stack_string[0][i] != " "]
        stacks = [[] for _ in range(len(column_index))]

        for row in stack_string[1:]:
            for j, col in enumerate(column_index):
                if col >= len(row):
                    continue
                if row[col] != " ":
                    stacks[j].append(row[col])

        # Parse the instructions
        i += 1
        instruction_string = self.input[i:]
        for i_s in instruction_string:
            i_s = i_s.replace("move ", "")
            quantity, out_in = i_s.split(" from ")
            out, input = out_in.split(" to ")
            instructions.append((int(quantity), int(out) - 1, int(input) - 1))

        return stacks, instructions

    def part_a(self):
        """
        Move a crate by crate
        """
        stacks, instructions = self.parse_input()
        for (quantity, source, output) in instructions:
            for _ in range(quantity):
                stacks[output].append(stacks[source].pop())

        output_string = ""
        for stack in stacks:
            output_string += stack.pop()
        return output_string

    def part_b(self):
        """
        Move all the crates in one go
        """
        stacks, instructions = self.parse_input()
        for (quantity, source, output) in instructions:
            stacks[output].extend(stacks[source][-quantity:])
            for _ in range(quantity):
                stacks[source].pop()

        output_string = ""
        for stack in stacks:
            output_string += stack.pop()
        return output_string


if __name__ == '__main__':
    (Day5()).run()
