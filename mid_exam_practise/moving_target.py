def remove(index, value):
    index = int(index)
    value = int(value)
    if 0 <= index < len(targets):
        targets[index] -= value
        if targets[index] <= 0:
            targets.pop(index)
    return index


def command_add(add_list, index, value):
    index = int(index)
    value = int(value)
    if 0 <= index < len(targets):
        add_list.insert(index, value)
    else:
        print("Invalid placement!")
    return add_list

def command_strike(index, value):
    index = int(index)
    value = int(value)
    if index < value or (value + index) >= len(targets):
        print("Strike missed!")
    else:
        del targets[index - value:index + value + 1]


targets = list(map(int, input().split()))
command = input().split()
new_list = []
while command[0] != "End":
    current_command = command[0]
    current_index = command[1]
    current_value = command[2]
    if current_command == "Shoot":
        action = remove(current_index, current_value)
    elif current_command == "Add":
        action = command_add(current_command, current_index, current_value)
    elif current_command == "Strike":
        action = command_strike(current_index, current_value)

    command = input().split()

print("|".join(map(str, targets)))
