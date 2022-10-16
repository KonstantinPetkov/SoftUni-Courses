number = int(input())
train = [0] * number
command = input()
while command != 'End':

    split_command = command.split(" ")
    current_command = split_command[0]

    if current_command == 'add':
        people_add = int(split_command[1])
        train[-1] += people_add
    elif current_command == 'insert':
        index = int(split_command[1])
        number_of_people = int(split_command[2])
        train[index] += number_of_people
    elif current_command == 'leave':
        index = int(split_command[1])
        people_to_leave = int(split_command[2])
        train[index] -= people_to_leave

    command = input()

print(train)