start_number = int(input())
end_number = int(input())
magic_number = int(input())

found_magic_boolaen = False
found_magic = False
counter = 0

for num1 in range(start_number, end_number + 1):
    for num2 in range(start_number, end_number + 1):
        counter += 1
        if num1 + num2 == magic_number:
            found_magic_boolaen = True
            found_magic = True
            print(f"Combination N:{counter} ({num1} + {num2} = {magic_number})")
            break
    if found_magic:
        break

if not found_magic:
    print(f"{counter} combinations - neither equals {magic_number}")
