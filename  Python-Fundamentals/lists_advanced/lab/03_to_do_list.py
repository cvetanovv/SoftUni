to_do_list = ["."] * 11

while True:
    command = input()
    if command == 'End':
        while "." in to_do_list:
            to_do_list.remove(".")
        print(to_do_list)
        break
    command = command.split("-")
    position = int(command[0])
    note = command[1]
    to_do_list.pop(position)
    to_do_list.insert(position, note)