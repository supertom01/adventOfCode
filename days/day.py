import parsers


class Day:

    def __init__(self, day_nr: int, description: str, input_type="int"):
        self.description = description
        if input_type == "int":
            self.input = parsers.parse_input_int(day_nr)
        elif input_type == "float":
            self.input = parsers.parse_input_float(day_nr)
        elif input_type == "str":
            self.input = parsers.parse_input_str(day_nr)
        else:
            raise RuntimeError(f"Invalid input type given: {input_type}")

    def part_a(self):
        """
        Calculates the solution for the first part of the days puzzle
        :return: The solution
        """
        return -1

    def part_b(self):
        """
        Calculates the solution for the second part of the days puzzle
        :return: The solution
        """
        return -1

    def run(self):
        print(f'\tPart A: {self.part_a()}')
        print(f'\tPart B: {self.part_b()}')

    def __str__(self):
        return self.description