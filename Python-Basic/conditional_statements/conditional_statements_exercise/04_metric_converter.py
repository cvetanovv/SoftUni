number = float(input())
from_unit = input()
to_unit = input()

if from_unit == 'mm' and to_unit == 'cm':
    result = number / 10
    print(f"{result:.3f}")
elif from_unit == 'mm' and to_unit == 'm':
    result = number / 1000
    print(f"{result:.3f}")
elif from_unit == 'cm' and to_unit == 'mm':
    result = number * 10
    print(f"{result:.3f}")
elif from_unit == 'cm' and to_unit == 'm':
    result = number / 100
    print(f"{result:.3f}")
elif from_unit == 'm' and to_unit == 'cm':
    result = number * 100
    print(f"{result:.3f}")
elif from_unit == 'm' and to_unit == 'mm':
    result = number * 1000
    print(f"{result:.3f}")