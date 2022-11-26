message = input()
while True:
    command = input()
    if command == "Reveal":
        break

    current_command = command.split(":|:")
    first_command = current_command[0]
    if first_command == "InsertSpace":
        index = int(current_command[1])
        if 0 <= index < len(message):
            message = message[:index] + " " + message[index:]
    elif first_command == "Reverse":
        substring = current_command[1]
        if substring in message:
            find_substring = message.find(substring)
            message = message[:find_substring] + message[find_substring + len(substring):]
            reversed_substring = substring[::-1]
            message += reversed_substring
        else:
            print("error")
            continue
    elif first_command == "ChangeAll":
        new_substring = current_command[1]
        replacement = current_command[2]
        message = message.replace(new_substring, replacement)

    print(message)

print(f"You have a new text message: {message}")
