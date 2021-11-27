import re

number_of_iterations = int(input())

pattern = r"^(@#+)([A-Z][a-zA-Z0-9]{4,}[A-Z])(@#+)$"

for _ in range(number_of_iterations):
    Flag = False
    product = input()
    matched_product = re.finditer(pattern, product)
    for match in matched_product:
        number_as_string = ""
        for char in match.group(2):
            if char.isdigit():
                number_as_string += char
        if number_as_string:
            print(f"Product group: {number_as_string}")
            Flag = True
        else:
            print("Product group: 00")
            Flag = True
    if not Flag:
        print("Invalid barcode")