def length_is_valid(name) -> bool:
    if 3 <= len(name) <= 16:
        return True
    return False


def symbols_are_valid(name) -> bool:
    for character in name:
        if not(character.isalnum() or character == "-" or character == "_"):
            return False
    return True


def no_redundant_symbols(name) -> bool:
    if " " in name:
        return False
    return True


def is_username_valid(name: str) -> bool:
    if length_is_valid(name) and symbols_are_valid(name) and no_redundant_symbols(name):
        return True
    return False


usernames = input().split(", ")

for user in usernames:
    if is_username_valid(user):
        print(user)
