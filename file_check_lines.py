def check_lines(f):
    with open(".\pwd_vault.txt", 'r') as f:
        count = len(f.readlines())
        print(count)
    return count



check_lines("\pwd_vault.txt")