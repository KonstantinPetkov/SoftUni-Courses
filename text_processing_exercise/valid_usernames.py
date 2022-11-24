def is_length_valid(name):
    if 3 <= len(name) <= 16:
        return True
    return False


def contain_character(character):
    for char in character:
        if not (char.isalnum() or char == "-" or char == "_"):
            return False
    return True


def no_redundant_symbols(name):
    if ' ' in name:
        return False
    return True


usernames = input().split(", ")

for username in usernames:
    if is_length_valid(username) and contain_character(username) and no_redundant_symbols(username):
        print(username)