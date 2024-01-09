# Importing functions and variables from settings.py
from settings import *
# Importing functions and variables from errors.py
from errors import *
# Importing functions and variables from syntaxInspector.py
from syntaxInspector import *


def string_to_char_list(string):
    """
    converts a string into a list of individual characters.
    :param string: a string
    :return: a list of string's extracted characters
    """
    list_of_chars = []

    for char in string:
        list_of_chars.append(char)
    return list_of_chars


def merge_numerical_tokens(list_of_tokens):
    """
    merges consecutive digits (including decimal points)
    within the list into their combined numerical values
    :param list_of_tokens: a list of individual chars
    :return: a list with merged members
    """
    combined_tokens_list = []
    current = ""

    while list_of_tokens:
        member = list_of_tokens[0]
        # checks if there is something to merge
        if member.isdigit() or member == '.':
            current += member
        else:
            if current:
                current = convert_type(current)
                combined_tokens_list.append(current)
            current = ""
            combined_tokens_list.append(member)
        # removes the current member
        list_of_tokens.remove(member)
    # adds the last member
    if current:
        current = convert_type(current)
        combined_tokens_list.append(current)
    return combined_tokens_list


def convert_type(string_to_convert):
    try:
        num = int(string_to_convert)
    except ValueError:
        num = float(string_to_convert)
    return num


def check_input_validation(user_input):
    """
    checks if user's input contains invalid chars
    :param user_input: a list of user's input
    :return: true if valid, false if not
    """
    for member in user_input:
        if member not in symbol_intensity_map:
            if not is_number(member):
                if member != ')' and member != '(':
                    return False
    return True


def is_number(string):
    """
    checks if the content of a string is a number
    :param string: a string
    :return: True if a number, false if not
    """
    try:
        float(string)
        return True
    except ValueError:
        return False


def get_user_input():
    """
    gets user's input until valid
    :return: a list of arithmetic expression
    """
    math_expression_list = []

    math_expression = input("Please enter an arithmetic expression: ")
    math_expression_list = string_to_char_list(math_expression)
    math_expression_list = merge_numerical_tokens(math_expression_list)
    if not check_input_validation(math_expression_list):
        raise InvalidInputError()
    return math_expression_list


def extract_from_brackets(expression_list):
    current_sub_expression = []
    current_position = 0
    start_position = 0
    count_open = 1
    count_close = 0

    if '(' in expression_list:
        start_position = expression_list.index('(')
        current_position = start_position
        if not check_brackets(expression_list):
            raise BracketsError()
        while current_position < len(expression_list) - 1:
            if expression_list[current_position + 1] == '(':
                count_open += 1
            elif expression_list[current_position + 1] == ')':
                count_close += 1
            if count_open == count_close:
                break
            else:
                current_sub_expression.append(expression_list[current_position + 1])
            current_position += 1
    return current_sub_expression, start_position, current_position + 1


def get_current_max_intensity(expression):
    """
    finds the current max intensity in the expression
    :param expression: list
    :return: current max intensity in the expression
    """
    max_intensity = 0
    for member in expression:
        if member in symbol_intensity_map:
            if symbol_intensity_map[member] > max_intensity:
                max_intensity = symbol_intensity_map[member]
    return max_intensity


def get_symbol_by_intensity(expression_list):
    """
    finds the first appearance of a symbol with the required intensity
    :param expression_list: a list
    :return: a symbol and its index in the list or 0 if not valid
    """
    intensity = get_current_max_intensity(expression_list)
    for member in expression_list:
        if member in symbol_intensity_map:
            if symbol_intensity_map[member] == intensity:
                return member, expression_list.index(member)
    return intensity, 0


def append_to_certain_index(members, to_append, index):
    """
    appends a required member to a list in a given index
    :param members: a list
    :param to_append: a member to append
    :param index: an index in the list
    :return: new list with appended member
    """
    new_list = []

    if not members:
        new_list.append(to_append)
    else:
        current_index = 0
        while len(members) > current_index:
            if current_index == index:
                new_list.append(to_append)
            new_list.append(members[current_index])
            current_index += 1
    if len(members) == len(new_list):
        new_list.append(to_append)
    return new_list


def handle_brackets(expression_list):
    current_sub_expression = []
    current_position = 0
    start_position = 0

    current_sub_expression, start_position, current_position = extract_from_brackets(expression_list)
    result = solve_expression(current_sub_expression)
    return result, start_position, current_position


def solve_expression(expression_list):
    current_position = 0
    start_position = 0
    current_intensity = 0
    result = 0

    while len(expression_list) > 1:
        if '(' in expression_list:
            result, start_position, current_position = handle_brackets(expression_list)
        else:
            symbol, symbol_index = get_symbol_by_intensity(expression_list)
            if symbol == 0:
                raise InvalidInputError()
            result, start_position, current_position = symbol_check_point(expression_list, symbol, symbol_index)
        del expression_list[start_position:current_position + 1]
        expression_list = append_to_certain_index(expression_list, result, start_position)
    return expression_list[0]


def main():
    validation_flag = True

    print_instructions()
    while validation_flag:
        try:
            expression_list = get_user_input()
            validation_flag = False
        except InvalidInputError as invalidErr:
            print(invalidErr)
    try:
        result = solve_expression(expression_list)
        print(result)
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


if __name__ == '__main__':
    main()
