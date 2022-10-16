list_of_happiness = input().split(' ')
factor = int(input())
list_of_happiness = list(map(lambda x: int(x) * factor, list_of_happiness))
filtered_employees = list(filter(lambda x: x >= sum(list_of_happiness) / len(list_of_happiness), list_of_happiness))

if len(filtered_employees) >= len(list_of_happiness) / 2:
    print(f'Score: {len(filtered_employees)}/{len(list_of_happiness)}. Employees are happy!')
else:
    print(f'Score: {len(filtered_employees)}/{len(list_of_happiness)}. Employees are not happy!')


