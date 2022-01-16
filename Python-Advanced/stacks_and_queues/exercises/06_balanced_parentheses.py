sequence_of_parentheses = input()
open_parentheses = "{[("

parentheses = []
is_balanced = True

for char in sequence_of_parentheses:
    if len(parentheses) < 1 and char not in open_parentheses:
        is_balanced = False
        break
    if char in open_parentheses:
        parentheses.append(char)
    else:
        last_char = parentheses.pop()
        if f"{last_char}{char}" not in "(){}[]":
            is_balanced = False
            break

if is_balanced:
    print("YES")
else:
    print("NO")