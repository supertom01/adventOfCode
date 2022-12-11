from day_base import Day


class Day10(Day):

    def __init__(self):
        super().__init__(2022, 10, 'Cathode-Ray Tube', expected_a=13140, debug=False)

    def parse(self):
        program = []
        for line in self.input:
            if len(line) == 4:
                program.append(None)
            else:
                program.append(int(line[5:]))
        return program

    def part_a(self) -> int:
        program = self.parse()
        add_value = 0
        reg_value = 1
        signal_strength = 0
        executing = False
        for cycle in range(220):
            if cycle + 1 in [20, 60, 100, 140, 180, 220]:
                signal_strength += reg_value * (cycle + 1)
            if not executing:
                instruction = program.pop(0)
                if instruction is not None:
                    executing = True
                    add_value = instruction
            else:
                reg_value += add_value
                executing = False
        return signal_strength

    def part_b(self) -> int:
        program = self.parse()
        add_value = 0
        reg_value = 1
        crt_screen_row = ""
        crt = []
        executing = False
        cycle = 0
        while len(program) > 0:
            current_column = cycle % 40
            if cycle % 40 == 0:
                crt.append(crt_screen_row)
                crt_screen_row = ""

            # Draw pixel
            if current_column in [reg_value - 1, reg_value, reg_value + 1]:
                crt_screen_row += "#"
            else:
                crt_screen_row += "."

            if not executing:
                instruction = program.pop(0)
                if instruction is not None:
                    executing = True
                    add_value = instruction
            else:
                reg_value += add_value
                executing = False
            cycle += 1
        crt.append(crt_screen_row)

        for row in crt:
            print(row)


if __name__ == '__main__':
    (Day10()).run()
