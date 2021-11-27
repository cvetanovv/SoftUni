password = input()

command = input()

while command != "Done":
    command = command.split(" ")
    action = command[0]
    if action == "TakeOdd":
        new_password = ""
        for index in range(len(password)):
            if index % 2 != 0:
                new_password += password[index]
        password = new_password
        print(password)
    elif action == "Cut":
        start_index = int(command[1])
        length = int(command[2])
        password = password[0:start_index] + password[start_index + length:]
        print(password)
    elif action == "Substitute":
        substring = command[1]
        substitute = command[2]
        if substring in password:
            password = password.replace(substring, substitute)
            print(password)
        else:
            print("Nothing to replace!")
    command = input()

print(f"Your password is: {password}")
