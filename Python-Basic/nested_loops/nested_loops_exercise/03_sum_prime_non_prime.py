
prime_numbers = 0
non_prime_numbers = 0

while True:
    command = input()
    if command == 'stop':
        break
    number = int(command)
    if number < 0:
        print("Number is negative.")
        continue
    for i in range(2, number):
        if number % i == 0:
            non_prime_numbers += number
            break
    else:
        prime_numbers += number


print(f"Sum of all prime numbers is: {prime_numbers}")
print(f"Sum of all non prime numbers is: {non_prime_numbers}")
