number = int(input())
grades = {}
for num in range(number):
    name = input()
    grade = float(input())
    grades[name] = grades.get(name, {})
    grades[name][grade] = grade

for student in grades.keys():
    result = 0
    for key, value in grades[student].items():
        result += value
    avr_score = result / len(grades[student])
    if avr_score >= 4.50:
        print(f"{student} -> {avr_score:.2f}")