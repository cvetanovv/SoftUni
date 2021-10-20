number_of_electrons = int(input())
counter = 0

result = []

for i in range(1, number_of_electrons + 1):
    electron = 2 * pow(i, 2)
    result.append(electron)
    counter += electron
    if sum(result) == result:
        break
    if counter + electron >= number_of_electrons:
        last_electron = number_of_electrons - counter
        if last_electron == 0:
            break
        else:
            result.append(last_electron)
            break

print(result)