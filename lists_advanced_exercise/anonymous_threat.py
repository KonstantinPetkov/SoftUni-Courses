def action_func(command):
    new_command = input()
    while new_command != "3:1":
        current_command = new_command.split()
        action, first_num, second_num = current_command[0], int(current_command[1]), int(current_command[2])

        if action == "merge":
            if first_num < 0:
                first_num = 0
            if first_num < second_num:
                if second_num >= len(data):
                    second_num = len(data) - 1
                for num in range(first_num, second_num):
                    data[first_num] += f"{data.pop(first_num + 1)}"

        elif action == "divide":
            index_length = len(data[first_num])
            space = index_length // second_num
            change_str = data.pop(first_num)
            changable_list = []
            for element in range(second_num - 1):
                changable_list.append(change_str[:space])
                change_str = change_str[space:]
            changable_list.append(change_str)
            for element in changable_list[::-1]:
                data.insert(first_num, element)

        new_command = input()

    return command


data = input().split()
result = action_func(data)
print(' '.join(result))
