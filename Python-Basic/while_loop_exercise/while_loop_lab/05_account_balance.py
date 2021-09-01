money = input()

sum = 0

while money != 'NoMoreMoney':
    money = float(money)
    if money < 0:
        print('Invalid operation!')
        break
    print(f"Increase: {money:.2f}")
    sum += money
    money = input()

print(f"Total: {sum:.2f}")