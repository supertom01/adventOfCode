import enum
from copy import deepcopy

from day_base import Day


class Instruction(enum.Enum):
    """
    A boot code instruction
    """
    ACCUMULATOR = 1     # Increase the accumulator with a given value
    JUMP = 2            # Jump a value amount of lines further
    NO_OPERATION = 3    # Do nothing


def calculate_acc(instructions):
    """
    Determine the final value of the accumulator at the end of a non-looping instruction set.
    :param instructions: The non-looping instruction set.
    :return:
    """
    current_line = 0
    accumulator = 0

    while current_line != len(instructions):
        command, value = instructions[current_line]
        if command == Instruction.JUMP:
            current_line += value
            continue
        elif command == Instruction.ACCUMULATOR:
            accumulator += value
        current_line += 1
    return accumulator


def is_looping(instructions):
    """
    Check if a given instruction set is causing an infinite loop
    :param instructions: The instruction set to check
    :return:
    """
    visited_lines = set()
    current_line = 0
    instruction_length = len(instructions)

    while True:
        # Check if we have already visited this line
        if current_line in visited_lines:
            return True
        else:
            visited_lines.add(current_line)

        # Check if the program has terminated
        if instruction_length == current_line:
            return False
        elif instruction_length < current_line:
            print(f"Warning: We're too far gone from the last instructions ({current_line - instruction_length} too much)")

        command, value = instructions[current_line]
        if command == Instruction.JUMP:
            current_line += value
        else:
            current_line += 1


class Day8(Day):

    def __init__(self):
        super(Day8, self).__init__(2020, 8, "Handheld Halting", expected_a=5, expected_b=8)
        self.instructions = []

    def parse_input(self):
        """
        Transforms the instructions into enums and integer values and puts them in a list
        :return:
        """
        for line in self.input:
            command, value = line.split(" ")
            value = int(value)
            if command == "acc":
                self.instructions.append((Instruction.ACCUMULATOR, value))
            elif command == "jmp":
                self.instructions.append((Instruction.JUMP, value))
            else:
                self.instructions.append((Instruction.NO_OPERATION, value))

    def part_a(self):
        self.parse_input()
        accumulator = 0
        visited_lines = set()
        current_line = 0

        while True:
            if current_line in visited_lines:
                break
            else:
                visited_lines.add(current_line)
            command, value = self.instructions[current_line]
            if command == Instruction.JUMP:
                current_line += value
                continue
            elif command == Instruction.ACCUMULATOR:
                accumulator += value
            current_line += 1
        return accumulator

    def part_b(self):
        for i in range(len(self.instructions)):
            if self.instructions[i][0] == Instruction.ACCUMULATOR:
                continue
            copy_instructions = deepcopy(self.instructions)
            command, value = copy_instructions[i]
            if command == Instruction.JUMP:
                copy_instructions[i] = (Instruction.NO_OPERATION, value)
            else:
                copy_instructions[i] = (Instruction.JUMP, value)

            if not is_looping(copy_instructions):
                return calculate_acc(copy_instructions)


if __name__ == '__main__':
    (Day8()).run()

