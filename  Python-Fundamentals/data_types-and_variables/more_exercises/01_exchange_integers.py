first_number = int(input())
second_number = int(input())

temp_a = first_number
temb_b = second_number

first_number = second_number
second_number = temp_a

print('Before:')
print(f"a = {temp_a}")
print(f"b = {temb_b}")
print('After:')
print(f"a = {first_number}")
print(f"b = {second_number}")