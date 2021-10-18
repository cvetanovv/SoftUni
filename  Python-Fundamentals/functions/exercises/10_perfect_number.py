def perfect_number(num):
    counter = 0
    for n in range(1, num):
        if num % n == 0:
            counter += n
    if counter == num:
        return  "We have a perfect number!"
    else:
        return "It's not so perfect."


number = int(input())

print(perfect_number(number))