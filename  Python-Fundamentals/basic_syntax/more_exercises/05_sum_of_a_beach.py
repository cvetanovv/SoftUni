text = input()
lower_text = text.lower()

sun = lower_text.count('sun')
sand = lower_text.count('sand')
water = lower_text.count('water')
fish = lower_text.count('fish')

word_sum = sun + sand + water + fish
print(word_sum)
