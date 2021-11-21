text_input = input().upper()

final_string = ""

index = 0
current_number_index = 0
while index < len(text_input):
    if text_input[index].isdigit():
        if len(text_input) > index + 1 and text_input[index + 1].isdigit():
            number_as_string = text_input[index] + text_input[index + 1]
            number = int(number_as_string)
            final_string += text_input[current_number_index:index] * number
            current_number_index = index + 2
            index += 1
            continue
        number = int(text_input[index])
        final_string += text_input[current_number_index:index] * number
        current_number_index = index + 1
    index += 1

unique_symbols = len(set(final_string))
print(f"Unique symbols used: {unique_symbols}")
print(final_string)