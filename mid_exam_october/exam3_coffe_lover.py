names_of_coffees = input().split()
number_of_commands = int(input())
manipulated_list = names_of_coffees.copy()
for new_command in range(number_of_commands):
    current_command = input().split()
    command = current_command[0]
    if command == "Include":
        first_element = current_command[1]
        manipulated_list.append(first_element)

    elif command == "Remove":
        first_removed_element = current_command[1]
        if first_removed_element == "first":
            second_element_for_first_remove = int(current_command[2])
            if second_element_for_first_remove < len(manipulated_list):
                manipulated_list = manipulated_list[second_element_for_first_remove:]
        if first_removed_element == "last":
            second_element_for_last_remove = int(current_command[2])
            if second_element_for_last_remove < len(manipulated_list):
                manipulated_list = manipulated_list[:len(manipulated_list) - second_element_for_last_remove]

    elif command == "Prefer":
        first_prefered_coffee = int(current_command[1])
        second_prefered_coffee = int(current_command[2])

        if first_prefered_coffee >= 0 and first_prefered_coffee <= len(manipulated_list) and second_prefered_coffee >= 0 and second_prefered_coffee <= len(manipulated_list):
            manipulated_list[first_prefered_coffee], manipulated_list[second_prefered_coffee] = manipulated_list[second_prefered_coffee], manipulated_list[first_prefered_coffee]

    elif command == "Reverse":
        manipulated_list = manipulated_list[::-1]

print(f"Coffees:")
print(f"{' '.join(manipulated_list)}")