def char_long_validator(password):
    if 6 <= len(password) <= 10:
        return True
    else:
        return False


def two_digits_validator(password):
    counter = 0
    for char in password:
        if char.isdigit():
            counter += 1
            if counter == 2:
                return True
    return False


password = input()

if char_long_validator(password) and two_digits_validator(password) and password.isalnum():
    print("Password is valid")
if not char_long_validator(password):
    print("Password must be between 6 and 10 characters")
if not password.isalnum():
    print("Password must consist only of letters and digits")
if not two_digits_validator(password):
    print("Password must have at least 2 digits")