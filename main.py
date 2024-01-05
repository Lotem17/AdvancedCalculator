# Importing functions and variables from settings.py
from settings import *
# Importing functions and variables from math.py
from math import *
# Importing functions and variables from errors.py
from errors import *


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
                combined_tokens_list.append(current)
            current = ""
            combined_tokens_list.append(member)
        # removes the current member
        list_of_tokens.remove(member)
    # adds the last member
    if current:
        combined_tokens_list.append(current)
    return combined_tokens_list


def check_input_validation(user_input):
    """
    checks if user's input contains invalid chars
    :param user_input: a list of user's input
    :return: true if valid, false if not
    """
    for member in user_input:
        if member not in symbol_intensity_map:
            if not is_number(member):
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


def main():
    validation_flag = True

    print_instructions()
    while validation_flag:
        try:
            expression_list = get_user_input()
            validation_flag = False
        except InvalidInputError as invalidErr:
            print(invalidErr)


if __name__ == '__main__':
    main()
