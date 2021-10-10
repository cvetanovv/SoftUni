nums = input().split(' ')
numbers = []
for num in nums:
    numbers.append(int(num))
left_car_time = 0
right_car_time = 0

left_side = numbers[0: len(numbers) // 2]
right_side = numbers[(len(numbers) + 1) // 2::]

for number in left_side:
    number = number
    left_car_time += number
    if number == 0:
        left_car_time *= 0.80

for i in range(len(numbers) - 1, len(left_side), -1):
    number = numbers[i]
    right_car_time += number
    if number == 0:
        right_car_time *= 0.80

if left_car_time < right_car_time:
    print(f"The winner is left with total time: {left_car_time:.1f}")
else:
    print(f"The winner is right with total time: {right_car_time:.1f}")