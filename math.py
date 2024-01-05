# Importing functions and variables from errors.py
from errors import *


def factorial(num):
    """
    calculates the factorial of a num
    :param num: a natural num
    :return: result of factorial
    """
    if isinstance(num, float):
        raise UnexpectedTypeError()
    if num < 0:
        raise UnexpectedValueError()
    if num == 0:
        return 1
    else:
        return factorial(num - 1) * num


def negation(num):
    """
    changes the sign of a num
    :param num: any num
    :return: result of negation
    """
    return num * -1


def minimum(num1, num2):
    """
    finds the smallest num
    :param num1: any num1
    :param num2: any num2
    :return: the smallest num between 2
    """
    if num1 <= num2:
        return num1
    return num2


def maximum(num1, num2):
    """
    finds the biggest num
    :param num1: any num1
    :param num2: any num2
    :return: the biggest num between 2
    """
    if num1 >= num2:
        return num1
    return num2


def average(num1, num2):
    """
    calculates the average between 2 numbers
    :param num1: any num1
    :param num2: any num2
    :return: average num
    """
    return (num1 + num2) / 2


def remainder(num1, num2):
    """
    calculates the remainder of the division between 2 nums
    :param num1: any num1
    :param num2: any num2 except 0
    :return: remainder of the division between 2 nums
    """
    if num2 == 0:
        raise DivisionByZero()
    return num1 % num2


def power(num1, num2):
    """
    calculates pow
    :param num1: any num1
    :param num2: any num2
    :return: the result of pow
    """
    return num1 ** num2


def division(num1, num2):
    """
    calculates the  division between 2 nums
    :param num1: any num1
    :param num2: any num2 except 0
    :return: result of division between 2 nums
    """
    if num2 == 0:
        raise DivisionByZero()
    return num1 / num2


def multiplication(num1, num2):
    """
    calculates Multiplication between 2 nums
    :param num1: any num1
    :param num2: any num2
    :return: result of Multiplication between 2 nums
    """
    return num1 * num2


def subtraction(num1, num2):
    """
    calculates Subtraction between 2 nums
    :param num1: any num1
    :param num2: any num2
    :return: result of Subtraction between 2 nums
    """
    return num1 - num2


def addition(num1, num2):
    """
    calculates Addition between 2 nums
    :param num1: any num1
    :param num2: any num2
    :return: result of Addition between 2 nums
    """
    return num1 + num2
