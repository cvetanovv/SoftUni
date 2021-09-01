pool_volume_in_litres = int(input())
p1 = int(input())
p2 = int(input())
hours_worker_missing = float(input())

p1_litres = p1 * hours_worker_missing
p2_litres = p2 * hours_worker_missing
all_litres = p1_litres + p2_litres

if pool_volume_in_litres >= all_litres:
    pool_precent_filled = (all_litres / pool_volume_in_litres) * 100
    p1_precent = (p1_litres / all_litres) * 100
    p2_precent = (p2_litres / all_litres) * 100
    print(f"The pool is {pool_precent_filled:.2f}% full. Pipe 1: {p1_precent:.2f}%. Pipe 2: {p2_precent:.2f}%.")
else:
    water_more = all_litres - pool_volume_in_litres
    print(f"For {hours_worker_missing} hours the pool overflows with {water_more:.2f} liters.")