num_pages = int(input())
pages_read_one_hours = int(input())
days = int(input())

hours_need_to_read_book = num_pages / pages_read_one_hours
hours_need_to_read_per_day = hours_need_to_read_book / days
print(hours_need_to_read_per_day)