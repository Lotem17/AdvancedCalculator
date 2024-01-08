# Importing functions and variables from settings.py
from settings import *


class InvalidInputError(Exception):
    """
    Raising an invalid input error
    """

    def __str__(self):
        return f"{'InvalidInputError'} : {error_messages['InvalidInputError']}"


class UnexpectedTypeError(Exception):
    """
    Raising an unexpected type error
    """

    def __str__(self):
        return f"{'UnexpectedTypeError'} : {error_messages['UnexpectedTypeError']}"


class UnexpectedValueError(Exception):
    """
    Raising an unexpected type error
    """

    def __str__(self):
        return f"{'UnexpectedValueError'} : {error_messages['UnexpectedValueError']}"


class DivisionByZero(Exception):
    """
    Raising an unexpected type error
    """

    def __str__(self):
        return f"{'DivisionByZero'} : {error_messages['DivisionByZero']}"


class BracketsError(Exception):
    """
    Raising an unexpected type error
    """

    def __str__(self):
        return f"{'BracketsError'} : {error_messages['BracketsError']}"


class FactorialError(Exception):
    """
    Raising an unexpected type error
    """

    def __str__(self):
        return f"{'FactorialError'} : {error_messages['FactorialError']}"


class NegativeBaseFractionalExponent(Exception):
    """
    Raising an unexpected type error
    """

    def __str__(self):
        return f"{'NegativeBaseFractionalExponent'} : {error_messages['NegativeBaseFractionalExponent']}"


class NegationError(Exception):
    """
    Raising an unexpected type error
    """

    def __str__(self):
        return f"{'NegationError'} : {error_messages['NegationError']}"
