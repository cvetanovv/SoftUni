password = input()

command = input()

while command != "Complete":
    command = command.split()
    action = command[0]
    if action == "Make":
        index = int(command[2])
        if command[1] == "Upper":
            password = password[:index] + password[index].upper() + password[index + 1:]
            print(password)
        elif command[1] == "Lower":
            password = password[:index] + password[index].lower() + password[index + 1:]
            print(password)
    elif action == "Insert":
        index = int(command[1])
        char = command[2]
        password = password[:index] + char + password[index:]
        print(password)
    elif action == "Replace":
        char = command[1]
        value = int(command[2])
        value_sum = chr(ord(char) + value)
        password = password.replace(char, value_sum)
        print(password)
    elif action == "Validation":
        if len(password) < 8:
            print("Password must be at least 8 characters long!")
        letter_and_digits = 0
        upper_letter = 0
        lower_letter = 0
        digit = 0
        for letter in password:
            if not letter.isalnum() and letter != "_":
                letter_and_digits += 1
            if letter.isupper():
                upper_letter += 1
            if letter.islower():
                lower_letter += 1
            if letter.isdigit():
                digit += 1
        if letter_and_digits != 0:
            print("Password must consist only of letters, digits and _!")
        if upper_letter == 0:
            print("Password must consist at least one uppercase letter!")
        if lower_letter == 0:
            print("Password must consist at least one lowercase letter!")
        if digit == 0:
            print("Password must consist at least one digit!")
    command = input()