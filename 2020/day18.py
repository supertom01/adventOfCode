"""
Next time, just use ANTLR or some other parser generator framework...
This is just pain :(
"""
import enum
from day_base import Day


class Operands(enum.Enum):
    ADD = 0
    MULT = 1


def evaluate_equal(expression: str):
    """
    Evaluates an expression where + and * have equal precedence.

    :param expression: The expression to evaluate (may only contain single character numbers)
    :return: The result of this expression and possible the position at which we stopped parsing it
    """
    result = 0
    prev_op = None
    i = 0
    while i < len(expression):
        op = expression[i]
        if op == ")":
            return i, result
        elif op == "+":
            prev_op = Operands.ADD
        elif op == "*":
            prev_op = Operands.MULT
        else:
            if op == "(":
                j, value = evaluate_equal(expression[i + 1:])
                i += j + 1
            else:
                value = int(expression[i])
            if prev_op is None:
                result = value
            elif prev_op == Operands.ADD:
                result += value
            elif prev_op == Operands.MULT:
                result *= value
        i += 1
    return result


def evaluate_advanced(expression: str):
    """
    Evaluates an expression where + precedes * evaluation

    :param expression: The expression to evaluate (may only contain single character numbers)
    :return: The result of this expression and possible the position at which we stopped parsing it
    """
    result = 0
    prev_op = None
    i = 0
    temp_string = ""
    while i < len(expression):
        op = expression[i]
        if op == ")":
            temp_string += str(result)
            return i, eval(temp_string)
        elif op == "+":
            prev_op = Operands.ADD
        elif op == "*":
            i += 1
            temp_string += str(result) + "*"
            result = 0
            continue
        else:
            if op == "(":
                j, value = evaluate_advanced(expression[i + 1:])
                i += j + 1
            else:
                value = int(expression[i])
            if prev_op is None:
                result = value
            elif prev_op == Operands.ADD:
                result += value
        i += 1
    temp_string += str(result)
    return eval(temp_string)


class Day18(Day):

    def __init__(self):
        super().__init__(2020, 18, 'Operation Order', debug=False)

    def part_a(self) -> int:
        return sum(evaluate_equal(expression.replace(" ", "")) for expression in self.input)

    def part_b(self) -> int:
        return sum(evaluate_advanced(expression.replace(" ", "")) for expression in self.input)


if __name__ == '__main__':
    (Day18()).run()
