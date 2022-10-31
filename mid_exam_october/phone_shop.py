def action_func(type_of_item):

    command = input()
    while command != "End":
        current_command, phone = command.split(" - ")

        if current_command == "Add":
            if phone not in type_of_item:
                type_of_item.append(phone)

        elif current_command == "Remove":
            if phone in type_of_item:
                type_of_item.remove(phone)

        elif current_command == "Bonus phone":
            old_phone, new_phone = phone.split(":")
            if old_phone in type_of_item:
                old_phone_index = type_of_item.index(old_phone)
                type_of_item.insert(old_phone_index + 1, new_phone)

        elif current_command == "Last":
            if phone in type_of_item:
                type_of_item.remove(phone)
                type_of_item.append(phone)

        command = input()
    return type_of_item


list_of_phones = input().split(", ")
result = action_func(list_of_phones)
print(', '.join(result))