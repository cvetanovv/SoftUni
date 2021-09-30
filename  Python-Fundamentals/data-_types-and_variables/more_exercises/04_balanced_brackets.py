number_of_lines = int(input())

brackets = []
flag = False
for line in range(number_of_lines):
    char = input()
    if char in ['(', ')']:
        brackets.append(char)

if brackets[0] == '(' and brackets[1] == ')':
    print('BALANCED')
else:
    print('UNBALANCED')
