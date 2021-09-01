months = int(input())

all_month_electricity_bills = 0
water_bills = months * 20
internet_bills = months * 15


for month in range(months):
    electricity_bill = float(input())
    all_month_electricity_bills += electricity_bill

other_bills = (all_month_electricity_bills + water_bills + internet_bills) * 1.20
average_bills = (all_month_electricity_bills + water_bills + internet_bills + other_bills) / months

print(f"Electricity: {all_month_electricity_bills:.2f} lv")
print(f"Water: {water_bills:.2f} lv")
print(f"Internet: {internet_bills:.2f} lv")
print(f"Other: {other_bills:.2f} lv")
print(f"Average: {average_bills:.2f} lv")