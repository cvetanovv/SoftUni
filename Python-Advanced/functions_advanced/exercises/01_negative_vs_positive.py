numbers = [int(x) for x in input().split()]

positive_numbers = [num for num in numbers if num > 0]
negative_numbers = [num for num in numbers if num < 0]

print(sum(negative_numbers))
print(sum(positive_numbers))


if abs(sum(positive_numbers)) > abs(sum(negative_numbers)):
    print("The positives are stronger than the negatives")
else:
    print("The negatives are stronger than the positives")