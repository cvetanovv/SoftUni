raw_key = input()

command = input()

while command != "Generate":
    command = command.split(">>>")
    action = command[0]
    if action == "Contains":
        substring = command[1]
        if substring in raw_key:
            print(f"{raw_key} contains {substring}")
        else:
            print("Substring not found!")
    elif action == "Flip":
        temporary_key = ''
        type_case, start_index, end_index = command[1:]
        start_index = int(start_index)
        end_index = int(end_index)
        if type_case == "Upper":
            temporary_key = raw_key[start_index:end_index].upper()
            raw_key = raw_key[:start_index] + temporary_key + raw_key[end_index:]
            print(raw_key)
        elif type_case == "Lower":
            temporary_key = raw_key[start_index:end_index].lower()
            raw_key = raw_key[:start_index] + temporary_key + raw_key[end_index:]
            print(raw_key)
    elif action == "Slice":
        start_index = int(command[1])
        end_index = int(command[2])
        raw_key = raw_key[0:start_index] + raw_key[end_index:]
        print(raw_key)
    command = input()

print(f"Your activation key is: {raw_key}")