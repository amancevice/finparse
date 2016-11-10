""" Module to parse a number-string to a float or decimal. """

import re

__version__ = '0.0.1'


def sign_string(string, sign=1):
    """ Determine what sign the string should be based on if it is wrapped
        within parenthesis. """
    try:
        for match in re.match(r'^\((.*?)\)$', string).groups():
            return sign_string(match, sign * -1)
    except AttributeError:
        return sign, string


def strip(string, decimal='.'):
    """ Strip non-decimal characters out of string. """
    return re.sub(r'[^\d{}]+'.format(decimal), '', string)


def parse(string, decimal='.', cast=float):
    """ Parse a string to a number object. """
    sign, string = sign_string(string)
    string = strip(string, decimal)
    string = string.replace(decimal, '.')
    return cast(string) * sign
