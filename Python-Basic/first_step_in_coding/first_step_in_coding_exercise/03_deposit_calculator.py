deposit_sum = float(input())
term_of_deposit_in_month = int(input())
annual_interest_rate = float(input())
annual_interest_rate /= 100

interest = deposit_sum * annual_interest_rate
one_month_interest = interest / 12

sum = deposit_sum + (term_of_deposit_in_month * one_month_interest)
print(sum)