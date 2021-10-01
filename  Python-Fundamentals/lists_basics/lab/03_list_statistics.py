number_of_iterations = int(input())

positive_numbers = []
negative_numbers = []

for n in range(number_of_iterations):
    number = int(input())
    if number >= 0:
        positive_numbers.append(number)
    else:
        negative_numbers.append(number)

print(positive_numbers)
print(negative_numbers)

count_positive_numbers = len(positive_numbers)
sum_negative_numbers = sum(negative_numbers)

print(f"Count of positives: {count_positive_numbers}")
print(f"Sum of negatives: {sum_negative_numbers}")