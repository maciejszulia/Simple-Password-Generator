import os

PWD_VAULT = "PWD_VAULT.txt"
PWD_PATH = os.path.dirname(os.path.abspath(PWD_VAULT))


def check_lines(f):
    with open("PWD_VAULT.txt", 'r') as f:
        count = len(f.readlines())
    return count


def create_vault():
    with open(PWD_VAULT, 'x') as f:
        pass
    print(f"PASSWORD VAULT NOT FOUND \n{PWD_VAULT} created at {PWD_PATH}\\")


def check_vault():
    if os.path.isfile(PWD_VAULT):
        print(f"Found {PWD_VAULT} at {PWD_PATH}\\ and "
              f"it contains {check_lines(PWD_VAULT)} passwords")
    else:
        create_vault()
    """todo: make this a encrypted mysql or other sql base"""


check_vault()
