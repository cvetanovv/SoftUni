def age_assignment(*names, **dict_ages):
    names_with_ages = {}
    for name in names:
        if name[0] in dict_ages:
            names_with_ages[name] = dict_ages[name[0]]
    return names_with_ages


print(age_assignment("Peter", "George", G=26, P=19))
print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))