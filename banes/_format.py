import re


def remove_extra_whitespaces(string):
    return re.sub(r'\s+', ' ', string)
