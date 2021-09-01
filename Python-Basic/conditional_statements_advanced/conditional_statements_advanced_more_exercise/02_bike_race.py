juniors_bicyclers = int(input())
seniors_bicyclers = int(input())
type_route = input()

tax = 0
all_bicyclers = juniors_bicyclers + seniors_bicyclers

if type_route == 'trail':
    tax = (juniors_bicyclers * 5.5) + seniors_bicyclers * 7
elif type_route == 'cross-country':
    tax = (juniors_bicyclers * 8) + seniors_bicyclers * 9.5
    if all_bicyclers >= 50:
        tax -= tax * 0.25
elif type_route == 'downhill':
    tax = (juniors_bicyclers * 12.25) + seniors_bicyclers * 13.75
elif type_route == 'road':
    tax = (juniors_bicyclers * 20) + seniors_bicyclers * 21.50


tax = tax * 0.95

print(f"{tax:.2f}")
