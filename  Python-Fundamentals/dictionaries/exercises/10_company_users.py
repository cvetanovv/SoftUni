companies = {}

while True:
    command = input()
    if command == "End":
        break
    company_name, employees_id = command.split(" -> ")
    if company_name not in companies:
        companies[company_name] = []

    if employees_id not in companies[company_name]:
        companies[company_name].append(employees_id)

sorted_companies = sorted(companies.items(), key=lambda kvp: kvp[0])

for company, empl_id in sorted_companies:
    print(company)
    for id in empl_id:
        print("-- ", end="")
        print("".join(id))
