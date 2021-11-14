def username_length(username):
    if 3 <= len(username) <= 16:
        return True
    return False


def username_contains(username):
    for char in username:
        if not char.isalnum() and char != "_" and char != "-":
            return False
    return True


def redundant_symbols(username):
    if " " in username:
        return False
    return True


def validator(username):
    if username_length(username) and username_contains(username) and redundant_symbols(username):
        return True
    else:
        return False


usernames = input().split(", ")

for user in usernames:
    if validator(user):
        print(user)