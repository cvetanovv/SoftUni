price_t_shirt = float(input())
needed_sum_for_ball = float(input())

price_shorts = price_t_shirt * 0.75
price_socks = price_shorts * 0.20
price_buttons = (price_t_shirt + price_shorts) * 2
all_sum = price_t_shirt + price_shorts + price_socks + price_buttons
sum_after_discount = all_sum - (all_sum * 0.15)

if sum_after_discount >= needed_sum_for_ball:
    print("Yes, he will earn the world-cup replica ball!")
    print(f"His sum is {sum_after_discount:.2f} lv.")
else:
    needed_money = needed_sum_for_ball - sum_after_discount
    print("No, he will not earn the world-cup replica ball.")
    print(f"He needs {needed_money:.2f} lv. more.")