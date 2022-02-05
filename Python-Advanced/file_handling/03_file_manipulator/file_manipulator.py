from os import path, remove

while True:
    line = input()
    if line == "End":
        break
    line_parts = line.split("-")
    command = line_parts[0]
    filename = line_parts[1]

    if command == "Create":
        open(filename, 'w').close()
    elif command == "Add":
        content = line_parts[2]
        with open(filename, 'a') as file:
            file.write(content + '\n')
    elif command == "Delete":
        if path.exists(filename):
            remove(filename)
        else:
            print("An error occurred")
    elif command == "Replace":
        old_string = line_parts[2]
        new_string = line_parts[3]

        if not path.exists(filename):
            print("An error occurred")
            continue

        with open(filename, 'r+') as file:
            new_file_content = file.read().replace(old_string, new_string)
            file.seek(0)
            file.truncate()
            file.write(new_file_content)