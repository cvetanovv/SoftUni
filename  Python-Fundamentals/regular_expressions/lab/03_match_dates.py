import re

pattern = r"(?P<Day>\b\d{2})([-\.\/])(?P<Month>[A-Z][a-z]{2})(\2)(?P<Year>\d{4}\b)"
text = input()

valid_dates = re.finditer(pattern, text)

for date in valid_dates:
    current_date = date.groupdict()
    print(f"Day: {current_date['Day']}, Month: {current_date['Month']}, Year: {current_date['Year']}")