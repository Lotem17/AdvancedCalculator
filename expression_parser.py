# This module is intended to create a list of operands and operators
# from the user's string while checking its validation

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


def convert_type(string_to_convert):
    """
    gets a string and tries to convert its type to int or float.
    if encounters ValueError issues, raises it
    :param string_to_convert:
    :return:
    """
    try:
        num = int(string_to_convert)
    except ValueError:
        try:
            num = float(string_to_convert)
        except ValueError:
            raise InvalidInputError
    return num


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


def check_input_validation(user_input):
    """
    checks if user's input contains invalid chars
    :param user_input: a list of user's input
    :return: true if valid, false if not
    """
    if not user_input:
        return False
    for member in user_input:
        if member not in symbol_intensity_map:
            if not is_number(member):
                if member != ')' and member != '(':
                    return False
    return True
