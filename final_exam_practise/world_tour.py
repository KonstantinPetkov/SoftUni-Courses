string = input()
while True:
    command = input()
    if command == "Travel":
        break

    current_command = command.split(":")
    first_command = current_command[0]
    if first_command == "Add Stop":
        index = int(current_command[1])
        new_string = current_command[2]
        if 0 <= index < len(string):
            string = string[:index] + new_string + string[index:]
    elif first_command == "Remove Stop":
        start_index = int(current_command[1])
        end_index = int(current_command[2])
        if 0 <= start_index < len(string) and 0 <= end_index < len(string):
            string = string[:start_index] + "" + string[end_index + 1:]
    elif first_command == "Switch":
        old_string = current_command[1]
        new_string = current_command[2]
        if old_string in string:
            string = string.replace(old_string, new_string)
    print(string)

print(f"Ready for world tour! Planned stops: {string}")


