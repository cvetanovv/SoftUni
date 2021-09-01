days = int(input())

treated_patients = 0
untreated_patients = 0
doctors = 7

for day in range(1, days + 1):
    patients = int(input())
    if day % 3 == 0:
        if untreated_patients > treated_patients:
            doctors += 1
    if doctors >= patients:
        treated_patients += patients
    if doctors < patients:
        untreated_patients += patients - doctors
        treated_patients += doctors

print(f"Treated patients: {treated_patients}.")
print(f"Untreated patients: {untreated_patients}.")