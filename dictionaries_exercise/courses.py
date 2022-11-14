courses = {}
while True:
    command = input()
    if command == "end":
        break
    course_name, student_name = command.split(" : ")
    courses[course_name] = courses.get(course_name, {})
    courses[course_name][student_name] = student_name

for name_of_course in courses.keys():
    print(f"{name_of_course}: {len(courses[name_of_course])}")
    for key, value in courses[name_of_course].items():
        print(f"-- {value}")

