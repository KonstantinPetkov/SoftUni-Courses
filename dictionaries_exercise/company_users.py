employees = {}

while True:
    command = input()
    if command == "End":
        break
    company_name, number = command.split(" -> ")
    employees[company_name] = employees.get(company_name, {})
    employees[company_name][number] = number

for name in employees.keys():
    print(f"{name}")
    for key, value in employees[name].items():
        print(f"-- {value}")
















