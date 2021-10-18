import string
import random

global PASSWORD


def get_password(password_len=8, has_lower=True, has_upper=True, has_special=False):
    available_cases = string.digits

    if has_lower is True:
        available_cases += string.ascii_lowercase
    if has_upper:
        available_cases += string.ascii_uppercase
    if has_special:
        available_cases += string.punctuation

    output = ""
    for i in range(password_len):
        output += available_cases[random.randint(0, len(available_cases) - 1)]

    return output
