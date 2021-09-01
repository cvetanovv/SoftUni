num_one = int(input())
num_two = int(input())
operator = input()

result = 0
even_or_odd = ''

if operator == '+':
    result = num_one + num_two
    if result % 2 == 0:
        even_or_odd = 'even'
    else:
        even_or_odd = 'odd'
    print(f"{num_one} {operator} {num_two} = {result} - {even_or_odd}")
elif operator == '-':
    result = num_one - num_two
    if result % 2 == 0:
        even_or_odd = 'even'
    else:
        even_or_odd = 'odd'
    print(f"{num_one} {operator} {num_two} = {result} - {even_or_odd}")
elif operator == '*':
    result = num_one * num_two
    if result % 2 == 0:
        even_or_odd = 'even'
    else:
        even_or_odd = 'odd'
    print(f"{num_one} {operator} {num_two} = {result} - {even_or_odd}")
elif operator == '/':
    if num_two == 0:
        print(f"Cannot divide {num_one} by zero")
    elif num_two != 0:
        result = num_one / num_two
        print(f"{num_one} {operator} {num_two} = {result:.2f}")
elif operator == '%':
    if num_two == 0:
        print(f"Cannot divide {num_one} by zero")
    elif num_two != 0:
        result = num_one % num_two
        print(f"{num_one} {operator} {num_two} = {result}")
