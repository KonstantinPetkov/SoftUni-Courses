text = input()
while True:
    command = input()
    if command == "Done":
        break

    current_command = command.split()
    new_command = current_command[0]

    if new_command == "Change":
        char, replacement = current_command[1], current_command[2]
        text = text.replace(char, replacement)
        print(text)

    elif new_command == "Includes":
        substring = current_command[1]
        if substring in text:
            print("True")
        else:
            print(f"False")

    elif new_command == "End":
        suffix = current_command[1]
        if text.endswith(suffix):
            print("True")
        else:
            print(f"False")

    elif new_command == "Uppercase":
        text = text.upper()
        print(text)

    elif new_command == "FindIndex":
        char = current_command[1]
        for index, ch in enumerate(text):
            if ch == char:
                print(index)
                break

    elif new_command == "Cut":
        start_index = int(current_command[1])
        count = int(current_command[2])
        if 0 <= start_index < len(text) and 0 <= count < len(text):
            text = text.replace(text[:start_index], "")
            text = text.replace(text[count:], "")
            print(text)
