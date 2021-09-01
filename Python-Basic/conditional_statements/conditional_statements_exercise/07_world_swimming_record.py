import math

record_in_seconds = float(input())
distance_in_meters = float(input())
time_in_sec_for_swiming_one_meter = float(input())

total_time_in_seconds = distance_in_meters * time_in_sec_for_swiming_one_meter
adding_seconds = math.floor(distance_in_meters / 15) * 12.5
total_time = total_time_in_seconds + adding_seconds

if total_time < record_in_seconds:
    print(f"Yes, he succeeded! The new world record is {total_time:.2f} seconds.")
else:
    needed_seconds = record_in_seconds - total_time
    needed_seconds = abs(needed_seconds)
    print(f"No, he failed! He was {needed_seconds:.2f} seconds slower.")