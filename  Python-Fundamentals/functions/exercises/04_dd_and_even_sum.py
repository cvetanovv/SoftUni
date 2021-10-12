def odd_even_sum(string_of_number):
    even_sum = 0
    odd_sum = 0
    for num in string_of_number:
        num = int(num)
        if num % 2 == 0:
            even_sum += num
        else:
            odd_sum += num
    print(f"Odd sum = {odd_sum}, Even sum = {even_sum}")


number = input()

odd_even_sum(number)