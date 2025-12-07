import operator
import re
from functools import reduce

from day_base import Day


class Day6(Day):

    def __init__(self):
        super().__init__(2025, 6, 'Trash Compactor', debug=False, expected_a=4277556, expected_b=3263827)
        
    def part_a(self):
        nr_of_problems = len([x for x in re.split(r'\s+', self.input[0]) if x.strip() != ''])
        problem_table = [[] for _ in range(nr_of_problems)]

        for line in self.input[:-1]:
            elements = [x for x in re.split(r'\s+', line) if x.strip() != '']
            for j, element in enumerate(elements):
                if element.strip() != '':
                    problem_table[j].append(int(element))

        total = 0
        for i, operation in enumerate(re.split(r'\s+', self.input[-1])):
            if operation == '*':
                total += reduce(operator.mul, problem_table[i], 1)

            elif operation == '+':
                total += sum(problem_table[i])

        return total

    def part_b(self):
        worksheet = [[x for x in line] for line in self.input]
        worksheet_length = len(worksheet)

        total = 0
        operation = None
        current_numbers = []
        for j in range(len(worksheet[0])):
            number = ""
            for i in range(len(worksheet)):
                x = worksheet[i][j]
                if i < worksheet_length - 1:
                    number += x
                else:
                    operation = x if x.strip() != '' else operation

            if number.strip() == '':
                # We've encountered an empty column
                if operation == '*':
                    total += reduce(operator.mul, current_numbers, 1)
                else:
                    total += sum(current_numbers)

                current_numbers = []
                operation = None
            else:
                current_numbers.append(int(number))

        # Run the last calculation
        if operation == '*':
            total += reduce(operator.mul, current_numbers, 1)
        else:
            total += sum(current_numbers)

        return total

if __name__ == '__main__':
    (Day6()).run()

