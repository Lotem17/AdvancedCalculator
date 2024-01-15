# This module is intended to solve the user's expression by finding the
# current prioritized part and solving it until the final result remains

# Importing functions and variables from syntax_inspector.py
from syntax_inspector import *
# Importing functions and variables from expression_parser.py
from expression_parser import *


def extract_from_brackets(expression_list):
    """
    extract an expression in brackets
    :param expression_list: a list of math
    :return: extracted expression and position in the list
    """
    current_sub_expression = []
    current_position = 0
    start_position = 0
    count_open = 1
    count_close = 0

    if '(' in expression_list:
        if not check_brackets(expression_list):
            raise BracketsError()
        start_position = expression_list.index('(')
        current_position = start_position

        while current_position < len(expression_list) - 1:
            # count opening and closing brackets
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


def handle_brackets(expression_list):
    """
    extracts and evaluates the sub-expression within brackets in an arithmetic expression
    :param expression_list: an arithmetic expression
    :return: the result along with the start and end positions of the extracted sub-expression
    """

    current_sub_expression, start_position, current_position = extract_from_brackets(expression_list)
    result = solve_expression(current_sub_expression)
    return result, start_position, current_position


def is_unary_minus(expression_list, index_of_minus):
    """
    determines if a minus is unary by the vars next to it
    :param expression_list: a list of math expression
    :param index_of_minus: the index of the minus
    :return: True if unary, False if not
    """
    next_in_list = expression_list[index_of_minus + 1]
    # unary minus does not have an expression before it
    if index_of_minus - 1 >= -len(expression_list) and (expression_list[index_of_minus - 1] in right_unary_symbols
                                                        or is_number(expression_list[index_of_minus - 1])):
        return False
    # unary minus has these operands after it
    if next_in_list == '(' or next_in_list == '-' or is_number(next_in_list):
        return True
    else:
        raise UnaryMinusError()


def has_minus_at_start(expression_list):
    """
    checks the last index of the unary minus in the beginning of the expression
    :param expression_list: a list of math expression
    :return: the last index
    """
    index = 0
    while index < len(expression_list) and expression_list[index] == '-':
        index += 1
    return index


def is_minus_to_append(expression_list, index):
    """
    checks if the priority of the unary minus is the highest
    :param expression_list: a list of math expression
    :param index: index of minus in the expression list
    :return: True if most prioritized, false if not
    """
    symbol, symbol_index = get_symbol_by_intensity(expression_list)
    # if the minus is in the beginning of the expression, it has priority over minus and plus,
    # otherwise, it has the highest priority
    if index + len(expression_list) < has_minus_at_start(expression_list):
        if symbol_intensity_map[symbol] != MIN_INTENSITY:
            return False
    return True


def handle_minus(expression_list):
    """
    combines consecutive unary minus signs with the following number in an arithmetic expression list.
    :param expression_list: a list of math expression
    """
    index = -1
    while index >= -len(expression_list):
        if expression_list[index] == '-':
            if is_unary_minus(expression_list, index) and is_minus_to_append(expression_list, index):
                expression_list[index] += str(expression_list[index + 1])
                expression_list[index] = shrink_minuses(expression_list[index])
                expression_list[index] = float(expression_list[index])
                del expression_list[index + 1]
                index = + 1
        index -= 1


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


def shrink_minuses(num_str):
    """
    determines if a num is positive or negative and deletes extra minuses
    :param num_str: a string of a number
    :return: the correct sign of the num
    """
    num = ""
    count = 0
    for member in num_str:
        if member == '-':
            count += 1
        else:
            num += member
    if count % 2 == 0:
        return num
    return '-' + num


def solve_expression(expression_list):
    """
    gets an arithmetical expression and solves it
    :param expression_list: a list of math expression
    :return: result
    """

    # while there is only one var in the list, which means all is solved and the list contains the result
    if not expression_list:
        return None
    while len(expression_list) > 1:
        if '(' in expression_list:
            result, start_position, current_position = handle_brackets(expression_list)
        else:
            handle_minus(expression_list)
            if len(expression_list) == 1:
                return expression_list[0]
            symbol, symbol_index = get_symbol_by_intensity(expression_list)
            if symbol == 0:
                raise InvalidInputError()
            result, start_position, current_position = symbol_check_point(expression_list, symbol, symbol_index)
        del expression_list[start_position:current_position + 1]
        expression_list = append_to_certain_index(expression_list, result, start_position)
    return expression_list[0]
