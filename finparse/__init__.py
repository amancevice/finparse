""" Module to parse a number-string to a float or decimal. """
import re

import pkg_resources

try:
    __version__ = pkg_resources.get_distribution(__package__).version
except pkg_resources.DistributionNotFound:  # pragma: no cover
    __version__ = None                      # pragma: no cover


def sign_string(string, sign=1):
    """ Determine what sign the string should be based on if it is wrapped
        within parenthesis. """
    try:
        # Try to unwrap numbers wrapped in ()s
        for match in re.match(r'^\((.*?)\)$', string).groups():
            return sign_string(match, sign * -1)
    except AttributeError:
        # Check for a negative sign in the string before returning
        return -int('-' in string) or sign, string


def strip(string, decimal='.'):
    """ Strip non-decimal characters out of string. """
    return re.sub(r'[^\d{}]+'.format(decimal), '', string)


def parse(string, decimal='.', cast=float):
    """ Parse a string to a number object. """
    string = str(string)
    pct = string.endswith('%')
    sign, string = sign_string(string)
    string = strip(string, decimal)
    string = string.replace(decimal, '.')
    value = cast(string) * sign / (100. ** pct)
    return value
