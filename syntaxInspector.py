# This module is intended to check the syntax of the symbols
# inside the list. if the syntax is valid, the result is returned


# Importing functions and variables from math.py
import math1
# Importing functions and variables from errors.py
from errors import *
# Importing functions and variables from expression_solver.py
import expression_solver


def check_range_end(expression, index):
    """
    checks if index out of range at the end of the list
    :param expression: a list
    :param index: index in the list
    :return: True if not in range, False if is
    """
    return index > len(expression) - 1


def check_range_start(index):
    """
    checks if index out of range at the beginning of the list
    :param index: index in the list
    :return: True if not in range, False if is
    """
    return index < 0


def is_number(num):
    """
    checks if is int or float
    :param num: a number
    :return: true if number, false if not
    """
    return isinstance(num, int) or isinstance(num, float)


def check_brackets(expression):
    """
    checks ife brackets are valid
    :param expression: a list of math expression
    :return: True if valid, false if not
    """
    if expression.count('(') != expression.count(')'):
        return False
    if expression.index('(') == expression.index(')') + 1:
        return False
    if expression.index(')') == expression.index('(') + 1:
        return False
    if expression.index(')') < expression.index('('):
        return False
    return True


def check_factorial(expression, index):
    """
    checks if factorial symbol is on the right side of a num
    :param expression: an arithmetical expression
    :param index: the index of the symbol
    :return: result of calculation, start and end position to delete
    """
    if check_range_start(index - 1):
        raise FactorialError()
    num = expression[index - 1]
    if is_number(num):
        result = math1.factorial(num)
        return result, index - 1, index
    raise FactorialError()


def check_hash(expression, index):
    """
    checks if hash symbol is on the right side of a num
    :param expression: an arithmetical expression
    :param index: the index of the symbol
    :return: result of calculation, start and end position to delete
    """
    if check_range_start(index - 1):
        raise SumNumbersError()
    num = expression[index - 1]
    if is_number(num):
        num = remove_dot_from_float(num)
        result = math1.sum_digits(num)
        return result, index - 1, index
    raise SumNumbersError()

def remove_dot_from_float(fnum):
    """
    removes dot from float num
    :param fnum: a float num
    :return: int num
    """
    int_num = ""
    fnum = str(fnum)
    new_num = fnum.split(".")
    for char in new_num:
        if char != ".":
            int_num += char
    int_num = int(int_num)
    return int_num

def check_negation(expression, index):
    """
    checks if tilda symbol is on the left side of a num
    :param expression: an arithmetical expression
    :param index: the index of the symbol
    :return: result of calculation, start and end position to delete
    """
    if check_range_end(expression, index + 1):
        raise NegationError()
    num = expression[index + 1]
    if num == '-':
        expression_solver.handle_minus(expression)
        num = expression[index + 1]
    if is_number(num):
        result = math1.negation(num)
        return result, index, index + 1
    raise NegationError()


def check_minimum(expression, index):
    """
    checks if mini symbol between numbers
    :param expression: an arithmetical expression
    :param index: the index of the symbol
    :return: result of calculation, start and end position to delete
    """
    if check_range_start(index - 1):
        raise MinimumError()
    if check_range_end(expression, index + 1):
        raise MinimumError()
    num1 = expression[index - 1]
    num2 = expression[index + 1]
    if is_number(num1) and is_number(num2):
        result = math1.minimum(num1, num2)
        return result, index - 1, index + 1
    raise MinimumError()


def check_maximum(expression, index):
    """
    checks if max symbol between numbers
    :param expression: an arithmetical expression
    :param index: the index of the symbol
    :return: result of calculation, start and end position to delete
    """
    if check_range_start(index - 1):
        raise MaximumError()
    if check_range_end(expression, index + 1):
        raise MaximumError()
    num1 = expression[index - 1]
    num2 = expression[index + 1]
    if is_number(num1) and is_number(num2):
        result = math1.maximum(num1, num2)
        return result, index - 1, index + 1
    raise MaximumError()


def check_average(expression, index):
    """
    checks if average symbol between numbers
    :param expression: an arithmetical expression
    :param index: the index of the symbol
    :return: result of calculation, start and end position to delete
    """
    if check_range_start(index - 1):
        raise AvgError()
    if check_range_end(expression, index + 1):
        raise AvgError()
    num1 = expression[index - 1]
    num2 = expression[index + 1]
    if is_number(num1) and is_number(num2):
        result = math1.average(num1, num2)
        return result, index - 1, index + 1
    raise AvgError()


def check_reminder(expression, index):
    """
    checks if modulu symbol between numbers
    :param expression: an arithmetical expression
    :param index: the index of the symbol
    :return: result of calculation, start and end position to delete
    """
    if check_range_start(index - 1):
        raise RemainderError()
    if check_range_end(expression, index + 1):
        raise RemainderError()
    num1 = expression[index - 1]
    num2 = expression[index + 1]
    if is_number(num1) and is_number(num2):
        result = math1.remainder(num1, num2)
        return result, index - 1, index + 1
    raise RemainderError()


def check_power(expression, index):
    """
    checks if power symbol between numbers
    :param expression: an arithmetical expression
    :param index: the index of the symbol
    :return: result of calculation, start and end position to delete
    """
    if check_range_start(index - 1):
        raise PowerError()
    if check_range_end(expression, index + 1):
        raise PowerError()
    num1 = expression[index - 1]
    num2 = expression[index + 1]
    if is_number(num1) and is_number(num2):
        result = math1.power(num1, num2)
        return result, index - 1, index + 1
    raise PowerError()


def check_division(expression, index):
    """
    checks if division symbol between numbers
    :param expression: an arithmetical expression
    :param index: the index of the symbol
    :return: result of calculation, start and end position to delete
    """
    if check_range_start(index - 1):
        raise DivError()
    if check_range_end(expression, index + 1):
        raise DivError()
    num1 = expression[index - 1]
    num2 = expression[index + 1]
    if is_number(num1) and is_number(num2):
        result = math1.division(num1, num2)
        return result, index - 1, index + 1
    raise DivError()


def check_mul(expression, index):
    """
    checks if multiplication symbol between numbers
    :param expression: an arithmetical expression
    :param index: the index of the symbol
    :return: result of calculation, start and end position to delete
    """
    if check_range_start(index - 1):
        raise MulError()
    if check_range_end(expression, index + 1):
        raise MulError()
    num1 = expression[index - 1]
    num2 = expression[index + 1]
    if is_number(num1) and is_number(num2):
        result = math1.multiplication(num1, num2)
        return result, index - 1, index + 1
    raise MulError()


def check_sub(expression, index):
    """
    checks if subtraction symbol between numbers
    :param expression: an arithmetical expression
    :param index: the index of the symbol
    :return: result of calculation, start and end position to delete
    """
    if check_range_start(index - 1):
        raise SubError()
    if check_range_end(expression, index + 1):
        raise SubError()
    num1 = expression[index - 1]
    num2 = expression[index + 1]
    if is_number(num1) and is_number(num2):
        result = math1.subtraction(num1, num2)
        return result, index - 1, index + 1
    raise SubError()


def check_add(expression, index):
    """
    checks if addition symbol between numbers
    :param expression: an arithmetical expression
    :param index: the index of the symbol
    :return: result of calculation, start and end position to delete
    """
    if check_range_start(index - 1):
        raise AddError()
    if check_range_end(expression, index + 1):
        raise AddError()
    num1 = expression[index - 1]
    num2 = expression[index + 1]
    if is_number(num1) and is_number(num2):
        result = math1.addition(num1, num2)
        return result, index - 1, index + 1
    raise AddError()


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
        case "&":
            return check_minimum(expression, symbol_index)
        case "$":
            return check_maximum(expression, symbol_index)
        case "@":
            return check_average(expression, symbol_index)
        case "%":
            return check_reminder(expression, symbol_index)
        case "^":
            return check_power(expression, symbol_index)
        case "/":
            return check_division(expression, symbol_index)
        case "*":
            return check_mul(expression, symbol_index)
        case "-":
            return check_sub(expression, symbol_index)
        case "+":
            return check_add(expression, symbol_index)
        case "#":
            return check_hash(expression, symbol_index)
