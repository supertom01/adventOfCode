import requests
from os.path import dirname


class Day:

    def __init__(self, day_nr: int, description: str, input_type="int"):
        self.day_nr = day_nr
        self.description = description
        self.input = self._get_input()
        if input_type == "int":
            self.input = list(map(int, self.input))
        elif input_type == "float":
            self.input = list(map(float, self.input))

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

    def _get_input(self):
        """
        Grabs the input from the AoC website.
        :return: A list with values
        """
        cookie_file = open(f'{dirname(dirname(__file__))}/cookie.txt', 'r')
        try:
            session_key = cookie_file.read()
        finally:
            cookie_file.close()

        url = f"https://adventofcode.com/2021/day/{self.day_nr}/input"
        request = requests.get(url, cookies={'session': session_key})
        request.close()
        return request.text.splitlines()
