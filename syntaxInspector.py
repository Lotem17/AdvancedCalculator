# Importing functions and variables from math.py
import math
# Importing functions and variables from errors.py
from errors import *


def check_brackets(expression):
    """
    checks if expression has equal amount of opening and closing brackets
    :param expression: a list of math expression
    :return: True if valid, false if not
    """
    if expression.count('(') != expression.count(')'):
        return False
    return True


def check_factorial(expression, index):
    """
    checks if factorial symbol is on the right side of a num
    :param expression: an arithmetical expression
    :param index: the index of the symbol
    :return: result of calculation, start and end position to delete
    """
    if index - 1 < 0:
        raise FactorialError()
    num = expression[index - 1]
    if isinstance(num, int) or isinstance(num, float):
        result = math1.factorial(num)
        return result, index - 1, index
    raise FactorialError()


def check_negation(expression, index):
    """
    checks if factorial symbol is on the left side of a num
    :param expression: an arithmetical expression
    :param index: the index of the symbol
    :return: result of calculation, start and end position to delete
    """
    if index + 1 > len(expression) - 1:
        raise NegationError()
    num = expression[index + 1]
    if isinstance(num, int) or isinstance(num, float):
        result = math1.negation(num)
        return result, index, index + 1
    raise NegationError()


def symbol_check_point(expression, symbol, symbol_index):
    """
    directs a symbol to its matching function in order to check its validation in the expression
    :param expression: a list
    :param symbol: the current symbol to check
    :param symbol_index: current symbol's index
    :return: result if valid
    """
    match symbol:
        case "!":
            return check_factorial(expression, symbol_index)
        case "~":
            return check_negation(expression, symbol_index)
        # case "&":
        # case "$":
        # case "@":
        # case "%":
        # case "^":
        # case "/":
        # case "*":
        # case "-":
        # case "+":
