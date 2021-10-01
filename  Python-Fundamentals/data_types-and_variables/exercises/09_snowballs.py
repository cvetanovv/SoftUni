snowballs = int(input())

highest_snowball_value = 0
highest_weight_of_snowball = 0
highest_needed_time = 0
highest_quality = 0

for snowball in range(snowballs):
    weight_of_snowball = int(input())
    needed_time = int(input())
    quality = int(input())
    snowball_value = pow(weight_of_snowball / needed_time, quality)
    if snowball_value > highest_snowball_value:
        highest_snowball_value = snowball_value
        highest_weight_of_snowball = weight_of_snowball
        highest_needed_time = needed_time
        highest_quality = quality

print(f"{highest_weight_of_snowball} : {highest_needed_time} = {int(highest_snowball_value)} ({highest_quality})")