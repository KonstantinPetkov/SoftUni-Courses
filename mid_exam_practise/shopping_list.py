def groceries_func(groceries):
    command = input()
    while command != "Go Shopping!":
        new_command  = command.split()
        current_command = new_command[0]

        if current_command == "Urgent":
            first_item = new_command[1]
            if first_item not in groceries:
                groceries.insert(0, first_item)

        elif current_command == "Unnecessary":
            first_item = new_command[1]
            if first_item in groceries:
                groceries.remove(first_item)

        elif current_command == "Correct":
            old_item = new_command[1]
            new_item = new_command[2]
            if old_item in groceries:
                old_item_index = groceries.index(old_item)
                groceries[old_item_index] = new_item

        elif current_command == "Rearrange":
            first_item = new_command[1]
            if first_item in groceries:
                groceries.remove(first_item)
                groceries.append(first_item)

        command = input()

    return groceries


initial_list = input().split("!")
result = groceries_func(initial_list)
print(', '.join(result))