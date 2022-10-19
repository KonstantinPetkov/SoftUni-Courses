def add(lessons_list, title):
    if title not in lessons_list:
        lessons_list.append(title)
    return lessons_list


def insert(lessons_list, title, index):
    if title not in lessons_list:
        lessons_list.insert(index, title)
    return lessons_list


def remove(lessons_list, title):
    if title in lessons_list:
        title_index = lessons_list.index(title)
        if title_index + 1 in range(len(lessons_list)):
            if "Exercise" in lessons_list[title_index + 1]:
                lessons_list.pop(title_index + 1)
        lessons_list.remove(title)
    return lessons_list


def swap(lessons_list, first, second):
    if first in lessons_list and second in lessons_list:
        first_position = lessons_list.index(first)
        second_position = lessons_list.index(second)
        is_first_has_exercise = False
        is_second_has_exercise = False
        if first_position + 1 in range(len(lessons_list)):
            is_first_has_exercise = "Exercise" in lessons_list[first_position + 1]
        if second_position + 1 in range(len(lessons_list)):
            is_second_has_exercise = "Exercise" in lessons_list[second_position + 1]
        lessons_list[first_position], lessons_list[second_position] = lessons_list[second_position], lessons_list[first_position]
        if is_first_has_exercise and is_second_has_exercise:
            lessons_list[first_position + 1], lessons_list[second_position + 1] = lessons_list[second_position + 1], lessons_list[first_position + 1]
        elif not is_first_has_exercise and is_second_has_exercise:
            lessons_list.insert(first_position + 1, lessons_list.pop(second_position + 1))
        elif is_first_has_exercise and not is_second_has_exercise:
            lessons_list.insert(second_position + 1, lessons_list.pop(first_position + 1))
    return lessons_list


def exersice(lessons_list, title):
    if title in lessons_list and f"{title}-Exercise" not in lessons_list:
        index_of_lesson = lessons_list.index(title)
        lessons_list.insert(index_of_lesson + 1, f"{title}-Exercise")
    elif title not in lessons_list:
        lessons_list.append(title)
        lessons_list.append(f"{title}-Exercise")
    return lessons_list


lessons = input().split(", ")
command = input().split(":")
while command[0] != "course start":
    current_command = command[0]
    lesson_title = command[1]
    if len(command) > 2:
        title_or_index = command[2]
    if current_command == "Add":
        lessons = add(lessons, lesson_title)
    elif current_command == "Insert":
        lessons = insert(lessons, lesson_title, int(title_or_index))
    elif current_command == "Remove":
        lessons = remove(lessons, lesson_title)
    elif current_command == "Swap":
        lessons = swap(lessons, lesson_title, title_or_index)
    elif current_command == "Exercise":
        lessons = exersice(lessons, lesson_title)
    command = input().split(":")

for index, name in enumerate(lessons):
    print(f"{index + 1}.{name}")
