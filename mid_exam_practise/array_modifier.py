numbers = list(map(int, input().split(" ")))
command = input()

while command != "end":
    current_command = command.split()
    new_command = current_command[0]
    if new_command == "swap":
        first_swap = int(current_command[1])
        second_swap = int(current_command[2])
        numbers[first_swap], numbers[second_swap] = numbers[second_swap], numbers[first_swap]
    elif new_command == "multiply":
        first_multiplayer = int(numbers[int(current_command[1])])
        second_multiplayer = int(numbers[int(current_command[2])])
        multiplayer = first_multiplayer * second_multiplayer
        numbers[int(current_command[1])] = multiplayer
    elif new_command == "decrease":
        for element in range(len(numbers)):
            numbers[element] -= 1

    command =input()

print(*numbers, sep=", ")