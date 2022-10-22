import math

number_of_students = int(input())
numbers_of_lectures = int(input())
additional_bonus = int(input())

max_attendaces = 0
max_points = 0

for student in range(number_of_students):
    student_attendaces = int(input())
    total_bonus = student_attendaces / numbers_of_lectures * (5 + additional_bonus)
    if total_bonus > max_points:
        max_points = total_bonus
        max_attendaces = student_attendaces

print(f"Max Bonus: {math.ceil(max_points)}.")
print(f"The student has attended {max_attendaces} lectures.")



