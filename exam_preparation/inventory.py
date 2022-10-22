def collecting_item(items):

    command = input()
    while command != "Craft!":
        current_command, item = command.split(" - ")

        if current_command == "Collect":
            if item not in items:
                items.append(item)

        elif current_command == "Drop":
            if item in items:
                items.remove(item)

        elif current_command == "Combine Items":
            old_item, new_item = item.split(":")
            if old_item in items:
                old_item_index = items.index(old_item)
                items.insert(old_item_index + 1, new_item)

        elif current_command == "Renew":
            if item in items:
                items.remove(item)
                items.append(item)

        command = input()

    return items


journal = input().split(", ")
data = collecting_item(journal)
print(', '.join(data))