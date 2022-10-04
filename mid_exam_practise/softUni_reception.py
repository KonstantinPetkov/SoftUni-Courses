first_employee_efficiency = int(input())
second_employee_efficiency = int(input())
third_employee_efficiency = int(input())
students_count = int(input())

sum_of_employee_efficiency = first_employee_efficiency + second_employee_efficiency + third_employee_efficiency
time_needed = 0

for time_needed in range(students_count):
    time_needed += 1

    if time_needed % 4 == 0:
        time_needed += 1
        continue

    if sum_of_employee_efficiency >= students_count:
        break

    students_count = students_count - sum_of_employee_efficiency

print(f"Time needed: {time_needed}h.")




