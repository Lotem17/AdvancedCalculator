# Importing functions and variables from expression_solver.py
from expression_solver import *


def get_user_input(math_expression):
    """
    gets user's input until valid
    :return: a list of arithmetic expression
    """
    math_expression_list = []
    math_expression_list = string_to_char_list(math_expression)
    math_expression_list = merge_numerical_tokens(math_expression_list)
    math_expression_list = delete_white_spaces(math_expression_list)
    if not check_input_validation(math_expression_list):
        raise InvalidInputError()
    return math_expression_list


def math_solver(expression_list):
    """
    gets the result from the expression solver or the error which raised
    :param expression_list: math expression
    :return: result
    """
    try:
        result = solve_expression(expression_list)
        return result
    except InvalidInputError as invalidErr:
        print(invalidErr)
    except BracketsError as bracketErr:
        print(bracketErr)
    except FactorialError as factorialErr:
        print(factorialErr)
    except DivisionByZero as zeroErr:
        print(zeroErr)
    except UnexpectedValueError as valueErr:
        print(valueErr)
    except UnexpectedTypeError as typeErr:
        print(typeErr)
    except NegationError as negErr:
        print(negErr)
    except MinimumError as miniErr:
        print(miniErr)
    except MaximumError as maxErr:
        print(maxErr)
    except AvgError as avgErr:
        print(avgErr)
    except RemainderError as rErr:
        print(rErr)
    except DivError as divErr:
        print(divErr)
    except PowerError as powErr:
        print(powErr)
    except MulError as mulErr:
        print(mulErr)
    except SubError as subErr:
        print(subErr)
    except AddError as addErr:
        print(addErr)
    except UnaryMinusError as minusErr:
        print(minusErr)
    except SumNumbersError as sumErr:
        print(sumErr)
    except NegativeBaseFractionalExponent as nErr:
        print(nErr)


def calculator(math_expression):
    """
    start calculator for test
    :param math_expression: input string
    :return:
    """
    try:
        expression_list = get_user_input(math_expression)
        result = math_solver(expression_list)
        return result
    except InvalidInputError as invalidErr:
        print(invalidErr)


def main():
    print_instructions()
    try:
        math_expression = input("Please enter an arithmetic expression: ")
        result = calculator(math_expression)
        if result is not None:
            if result >= MAX_VALID_NUM:
                result = 'inf'
            print(result)
    except EOFError as eofErr:
        print(eofErr)


if __name__ == '__main__':
    main()
