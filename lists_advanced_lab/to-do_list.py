tasks = []
while True:
    command = input()

    if command == 'End':
        break

    split_command = command.split('-')
    importance = int(split_command[0])
    note = split_command[1]
    tasks.append([importance, note])

sorted_tasks = []
for task in sorted(tasks):
    sorted_tasks.append(task[1])

print(sorted_tasks)

