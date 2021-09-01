
letter_counter = 0
n_counter = 0
c_counter = 0
o_counter = 0

while True:
    if letter_counter == 4:
        n_counter = 0
        c_counter = 0
        o_counter = 0
        letter_counter = 0
        break
    letter = input()
    if letter == 'End':
        break

    if n_counter > 0:
        if letter == 'n':
            print(letter, end='')
    if letter == 'n':
        n_counter += 1
        letter_counter += 1
        continue

    if o_counter > 0:
        if letter == 'o':
            print(letter, end='')
    if letter == 'o':
        o_counter += 1
        letter_counter += 1
        continue

    if c_counter > 0:
        if letter == 'c':
            print(letter, end='')
    if letter == 'c':
        c_counter += 1
        letter_counter += 1
        continue
    print(letter, end='')

print(end=' ')

while True:
    if letter_counter == 4:
        n_counter = 0
        c_counter = 0
        o_counter = 0
        letter_counter = 0
        break
    letter = input()
    if letter == 'End':
        break

    if n_counter > 0:
        if letter == 'n':
            print(letter, end='')
    if letter == 'n':
        n_counter += 1
        letter_counter += 1
        continue

    if o_counter > 0:
        if letter == 'o':
            print(letter, end='')
    if letter == 'o':
        o_counter += 1
        letter_counter += 1
        continue

    if c_counter > 0:
        if letter == 'c':
            print(letter, end='')
    if letter == 'c':
        c_counter += 1
        letter_counter += 1
        continue
    print(letter, end='')

