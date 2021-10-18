def data_type(input_type, data):
    if input_type == "int":
        data = int(data)
        return  data * 2
    elif input_type == "real":
        data = float(data)
        return f"{data * 1.5:.2f}"
    elif input_type == "string":
        return f"${data}$"


first_input = input()
second_input = input()

print(data_type(first_input, second_input))