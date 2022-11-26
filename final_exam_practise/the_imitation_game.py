string = input()
while True:
    command = input()
    if command == "Decode":
        break

    current_command = command.split("|")
    first_command = current_command[0]
    if first_command == "Move":
        number = int(current_command[1])
        string = string[number:] + string[:number]
    elif first_command == "Insert":
        num = int(current_command[1])
        value = current_command[2]
        string = string[:num] + value + string[num:]
    elif first_command == "ChangeAll":
        substring = current_command[1]
        replacment = current_command[2]
        string = string.replace(substring, replacment)

print(f"The decrypted message is: {string}")
