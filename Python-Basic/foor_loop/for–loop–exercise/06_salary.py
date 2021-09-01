open_tabs = int(input())
salary = float(input())

for x in range(open_tabs):
    websites = input()

    if websites == 'Facebook':
        salary -= 150
    elif websites == 'Instagram':
        salary -= 100
    elif websites == 'Reddit':
        salary -= 50
    if salary <= 0:
        break

if salary <= 0:
    print("You have lost your salary.")
else:
    print(int(salary))