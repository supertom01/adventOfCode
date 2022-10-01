import time
import requests
from os.path import dirname

"""
The Day class provides a framework for all the days that are created during the Advent of Code programming calendar.
This class provides the abstraction needed in order to make sure that only the actual algorithms need to be written
for each day and not the management around it.

Author: Tom Meulenkamp (https://github.com/supertom01)
Date: 03-12-2021
"""


class Day:

    def __init__(self, day_nr: int, description: str, **kwargs):
        """
        Creates a new day object.
        This object automatically fetches the input from the AoC website if needed, or reads the test input from a file.
        It provides abstractions like a run method in order to minimize the code that has to be written for each day.
        :param day_nr: The number of the day of the calendar (starting at 1)
        :param description: The description of today's puzzle
        :param kwargs: Optional arguments, like debug and input_type
                        debug => If True, reads test input instead of actual input, by default False
                        input_type => Determines how the input should be parsed, by default int
        """
        self.day_nr = day_nr
        self.description = description
        if "debug" in kwargs.keys() and kwargs.get("debug"):
            self.input = self._get_test()
        else:
            self.input = self._get_input()
        if "input_type" in kwargs.values():
            if kwargs.get("input_type") == "int":
                self.input = list(map(int, self.input))
            elif kwargs.get("input_type") == "float":
                self.input = list(map(float, self.input))
            else:
                raise RuntimeWarning(
                    f"Warning! Invalid input type provided: {kwargs.get('input_type')}. Defaulting to string.")

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
        """
        Executes each part of the day and measures the time it takes to execute it.
        """
        print(self)

        before = time.time()
        answer_a = self.part_a()
        after = time.time()
        print(f'\tPart A: {answer_a} (computation time: {(after - before) * 1000:.5f} ms)')

        before = time.time()
        answer_b = self.part_b()
        after = time.time()
        print(f'\tPart B: {answer_b} (computation time: {(after - before) * 1000:.5f} ms)')
        print()

    def __str__(self):
        return f"Day {self.day_nr} \"{self.description}\""

    def _get_test(self):
        """
        Grabs the test input from a text file.
        :return: A list with values
        """
        test_file = open(f'{dirname(dirname(__file__))}/test/{self.day_nr}.txt', 'r')
        try:
            return [line.replace("\r\n", "").replace("\n", "") for line in test_file.readlines()]
        finally:
            test_file.close()

    def _get_input(self):
        """
        Grabs the input from the AoC website.
        :return: A list with values
        """
        cookie_file = open(f'{dirname(__file__)}/cookie.txt', 'r')
        try:
            session_key = cookie_file.read()
        finally:
            cookie_file.close()

        url = f"https://adventofcode.com/2021/day/{self.day_nr}/input"
        request = requests.get(url, cookies={'session': session_key})
        request.close()
        return request.text.splitlines()
