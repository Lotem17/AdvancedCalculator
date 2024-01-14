MAX_INTENSITY = 6
MIN_INTENSITY = 1

right_unary_symbols = ["#", "!",]

# Mapping symbols to intensity levels
symbol_intensity_map = {
    "!": MAX_INTENSITY,
    "~": MAX_INTENSITY,
    "#": MAX_INTENSITY,
    "&": 5,
    "$": 5,
    "@": 5,
    "%": 4,
    "^": 3,
    "/": 2,
    "*": 2,
    "-": MIN_INTENSITY,
    "+": MIN_INTENSITY,
}

error_messages = {
    "InvalidInputError": "Invalid input. Please provide valid data.",
    "UnexpectedTypeError": "Received unexpected type of value. Please make sure the expression is valid. ",
    "UnexpectedValueError": "Received unexpected value. Please make sure the expression is valid. ",
    "DivisionByZero": "division or modulo by zero. ",
    "BracketsError": "Invalid usage of brackets. ",
    "FactorialError": "Invalid usage of factorial. ",
    "NegativeBaseFractionalExponent": "incorrect application of fractional exponentiation to a negative base.",
    "NegationError": "Invalid usage of negation. ",
    "MinimumError": "Invalid usage of minimum",
    "MaximumError": "Invalid usage of minimum",
    "AvgError": "Invalid usage of average",
    "RemainderError": "Invalid usage of remainder",
    "PowerError": "Invalid usage of power",
    "DivError": "Invalid usage of division",
    "MulError": "Invalid usage of multiplication",
    "SubError": "Invalid usage of subscription",
    "AddError": "Invalid usage of addition",
    "UnaryMinusError": "Unary minus must be beside -, ( or a num",
    "SumNumbersError": "Invalid usage of hash mark",
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
    print('12) # (Hash mark): Sum of digits')
    print("--------------------------------------------------------------------------------")
