number_of_days = int(input())
number_of_confectioners = int(input())
number_of_cakes = int(input())
number_of_waffles = int(input())
number_of_pancakes = int(input())

cake = 45
waffle = 5.80
pancake = 3.20
sum_one_day_products = (number_of_cakes * cake) + (number_of_waffles * waffle) + (number_of_pancakes * pancake)
sum_product_plus_confectioners = sum_one_day_products * number_of_confectioners

sum_all_campaing = sum_product_plus_confectioners * number_of_days
sum_after_costs = sum_all_campaing - (sum_all_campaing / 8)
print(sum_after_costs)