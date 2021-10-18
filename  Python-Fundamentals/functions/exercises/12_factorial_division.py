def factorial(number):
    fact = 1
    for i in range(1, number + 1):
        fact *= i
    return fact


first_number = int(input())
second_number = int(input())

fact_first_number = factorial(first_number)
fact_second_number = factorial(second_number)

result = fact_first_number / fact_second_number
print(f"{result:.2f}")