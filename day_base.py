import os.path
import time
import requests
from os.path import dirname

"""
The Day class provides a framework for all the days that are created during the Advent of Code programming calendar.
This class provides the abstraction needed in order to make sure that only the actual algorithms need to be written
for each day and not the management around it.

Author: Tom Meulenkamp (https://github.com/supertom01)
Date: 28-11-2022
"""


class Day:

    def __init__(self, year: int, day_nr: int, description: str, expected_a=None, expected_b=None, **kwargs):
        """
        Creates a new day object.
        This object automatically fetches the input from the AoC website if needed, or reads the test input from a file.
        It provides abstractions like a run method in order to minimize the code that has to be written for each day.
        :param year: The year of the current AoC
        :param day_nr: The number of the day of the calendar (starting at 1)
        :param description: The description of today's puzzle
        :param expected_a: The expected answer for the first part, given the example code
        :param expected_b: The expected answer for the second part, given the example code
        :param kwargs: Optional arguments, like debug and input_type
                        debug => If True, reads test input instead of actual input, by default False
                        input_type => Determines how the input should be parsed, by default int
        """
        self.year = year
        self.day_nr = day_nr
        self.description = description
        self.debug = "debug" in kwargs.keys() and kwargs.get("debug")
        self.expected_a = expected_a
        self.expected_b = expected_b
        if self.debug:
            self.input = self._get_test()
        else:
            self.input = self._get_input()

        if "input_type" in kwargs.keys():
            if not kwargs.get("input_type") == "raw":
                self.input = self.input.splitlines()
            if kwargs.get("input_type") == "int":
                self.input = list(map(int, self.input))
            elif kwargs.get("input_type") == "float":
                self.input = list(map(float, self.input))
            elif kwargs.get("input_type") == "str" or kwargs.get("input_type") == "raw":
                pass
            else:
                print(f"Warning! Invalid input type provided: {kwargs.get('input_type')}. Defaulting to string.")
        else:
            self.input = self.input.splitlines()

    def part_a(self) -> int:
        """
        Calculates the solution for the first part of the days puzzle
        :return: The solution
        """
        raise NotImplementedError("Part A has not yet been implemented")

    def part_b(self) -> int:
        """
        Calculates the solution for the second part of the days puzzle
        :return: The solution
        """
        raise NotImplementedError("Part B has not yet been implemented")

    def run(self) -> None:
        """
        Executes each part of the day and measures the time it takes to execute it.
        """
        print(self)

        answer_a = None
        answer_b = None
        try:
            before = time.time()
            answer_a = self.part_a()
            after = time.time()
            print(f'\tPart A: {answer_a} (computation time: {(after - before) * 1000:.5f} ms)')
        except NotImplementedError as error:
            print("\t", error)

        try:
            before = time.time()
            answer_b = self.part_b()
            after = time.time()
            print(f'\tPart B: {answer_b} (computation time: {(after - before) * 1000:.5f} ms)')
        except NotImplementedError as error:
            print("\t", error)
        print()

        # If we're in debug mode, check if the answers are as expected
        if self.debug:
            self.test(answer_a, answer_b)

    def test(self, answer_a, answer_b) -> None:
        """
        Compares the actual answers with expected answers as provided in the constructor
        :param answer_a: The answer as calculated by this day for part a
        :param answer_b: The answer as calculated by this day for part b
        """
        if self.expected_a is not None and answer_a is not None:
            assert self.expected_a == answer_a, f"Day {self.day_nr} Part A: Expected {self.expected_a} but got {answer_a}"
        if self.expected_b is not None and answer_b is not None:
            assert self.expected_b == answer_b, f"Day {self.day_nr} Part B: Expected {self.expected_b} but got {answer_b}"
        print("Test passed")

    def __str__(self) -> str:
        return f"Day {self.day_nr} \"{self.description}\""

    def _get_test(self) -> str:
        """
        Grabs the test input from a text file.
        :return: A list with values
        """
        test_file = open(f'{dirname(__file__)}/test/{self.year}/{self.day_nr}.txt', 'r')
        try:
            return test_file.read()
            #return [line.replace("\r\n", "").replace("\n", "") for line in test_file.readlines()]
        finally:
            test_file.close()

    def _get_input(self) -> str:
        """
        Grabs the input from the AoC website or from the cache if available.
        :return: The input for the daily puzzle. Every line has its own index in the returned list
        """
        # Check the cache for input and set up the needed directory structure if this does not exist yet.
        cache_path = f'{dirname(__file__)}/input/{self.year}/{self.day_nr}.txt'
        if os.path.exists(cache_path):
            # We already requested the input once, so just use this
            with open(cache_path, 'r') as input_file:
                return input_file.read()
        else:
            # Make sure that the directory structure does exist
            if not os.path.exists(f'{dirname(__file__)}/input'):
                os.mkdir(f'{dirname(__file__)}/input')
                os.mkdir(f'{dirname(__file__)}/input/{self.year}')
            elif not os.path.exists(f'{dirname(__file__)}/input/{self.year}'):
                os.mkdir(f'{dirname(__file__)}/input/{self.year}')

        # Make a request to the AoC website for our puzzle input
        cookie_file = open(f'{dirname(__file__)}/cookie.txt', 'r')
        try:
            session_key = cookie_file.read()
        finally:
            cookie_file.close()

        try:
            url = f"https://adventofcode.com/{self.year}/day/{self.day_nr}/input"
            request = requests.get(url, cookies={'session': session_key})
            request.close()
        except Exception:
            print(f"Error: Could not retrieve input data for day {self.day_nr}\r\nMake sure that you have an active internet connection")
            exit()

        # Cache the input for later use
        lines = request.text
        with open(cache_path, 'x') as input_file:
            input_file.write(lines)
        return lines
