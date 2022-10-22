def command_remove(index, power, targets):
    if 0 <= index < len(targets):
        targets[index] -= power
        if targets[index] <= 0:
            targets.pop(index)

    return targets


def command_add(index, value, targets):
    if 0 <= index < len(targets):
        targets.insert(index, value)
    else:
        print("Invalid placement!")

    return targets


def command_strike(index, radius, targets):
    validator = index - radius >= 0 and index + radius < len(targets)
    if validator:
        first_index = index - radius
        last_index = index + radius
        targets = [targets[i] for i in range(len(targets)) if i < first_index or i > last_index]
    else:
        print("Strike missed!")

    return targets


def action_func(targets):
    command = input()
    while command != "End":
        current_command, index, value = command.split()
        if current_command == "Shoot":
            targets = command_remove(int(index), int(value), targets)
        elif current_command == "Add":
            targets = command_add(int(index), int(value), targets)
        elif current_command == "Strike":
            targets = command_strike(int(index), int(value), targets)
        command = input()

    return targets

sequence_of_targets = list(map(int, input().split()))
result = action_func(sequence_of_targets)
print("|".join(map(str, result)))






