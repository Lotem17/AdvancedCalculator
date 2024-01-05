# Importing functions and variables from math.py
from math import *

# Mapping symbols to intensity levels
symbol_intensity_map = {
    "(": 7,
    ")": 7,
    "!": 6,
    "~": 6,
    "&": 5,
    "$": 5,
    "@": 5,
    "%": 4,
    "^": 3,
    "/": 2,
    "*": 2,
    "-": 1,
    "+": 1,
}

operation_symbols_map = {
    "!": factorial,
    "~": negation,
    "&": minimum,
    "$": maximum,
    "@": average,
    "%": remainder,
    "^": power,
    "/": division,
    "*": multiplication,
    "-": subtraction,
    "+": addition,
}

error_messages = {
    "InvalidInputError": "Invalid input. Please provide valid data.",
    "UnexpectedTypeError": "Received unexpected type of value. Please make sure the expression is valid. ",
    "UnexpectedValueError": "Received unexpected value. Please make sure the expression is valid. ",
    "DivisionByZero": "division or modulo by zero. "
}


def print_instructions():
    print("--------------------------------------------------------------------------------")
    print("Welcome to Omega's Advanced Calculator!")
    print("This calculator can perform arithmetic operations according to the list below:")
    print('1) ! (Exclamation Mark): Factorial')
    print('2) ~ (Tilde): Negation')
    print('3) & (Ampersand): Minimum')
    print('4) $ (Dollar Sign): Maximum')
    print('5) @ (At Sign): Average')
    print('6) % (Percentage Sign): Remainder')
    print('7) ^ (Caret): Power')
    print('8) / (Forward Slash): Division')
    print('9) * (Asterisk): Multiplication')
    print('10) - (Hyphen): Subtraction')
    print('11) + (Plus Sign): Addition')
    print("--------------------------------------------------------------------------------")
