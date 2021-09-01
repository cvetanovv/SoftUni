first_number = int(input())
second_number = int(input())


for number in range(first_number, second_number + 1):
    number = str(number)
    sum_odd_numbers = 0
    sum_even_numbers = 0

    for index, num in enumerate(number):
        if index % 2 == 0:
            sum_even_numbers += int(num)
        else:
            sum_odd_numbers += int(num)
    if sum_odd_numbers == sum_even_numbers:
        print(number, end= " ")
