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
