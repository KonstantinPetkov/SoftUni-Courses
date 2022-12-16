text = input()

while True:
    command = input()
    if command == "Finish":
        break
    current_command = command.split()
    decrypting = current_command[0]
    if decrypting == "Replace":
        current_char, new_char = current_command[1], current_command[2]
        text = text.replace(current_char, new_char)
        print(text)

    elif decrypting == "Cut":
        start_index, end_index = int(current_command[1]), int(current_command[2])
        if 0 <= start_index < len(text) and 0 <= end_index < len(text):
            text = text[:start_index] + "" + text[end_index + 1:]
            print(text)
        else:
            print("Invalid indices!")

    elif decrypting == "Make":
        upper_lower = current_command[1]
        if upper_lower == "Upper":
            for ch in text:
                if ch.islower():
                    upper_ch = ch.upper()
                    text = text.replace(ch, upper_ch)
        elif upper_lower == "Lower":
            for ch in text:
                if ch.isupper():
                    lower_ch = ch.lower()
                    text = text.replace(ch, lower_ch)
        print(text)

    elif decrypting == "Check":
        string = current_command[1]
        if string in text:
            print(f"Message contains {string}")
        else:
            print(f"Message doesn't contain {string}")

    elif decrypting == "Sum":
        started_index, ended_index = int(current_command[1]), int(current_command[2])
        if 0 <= started_index < len(text) and 0 <= ended_index < len(text):
            substring = text[started_index: ended_index + 1:]
            sum_char = 0
            for char in substring:
                new_char = ord(char)
                sum_char += new_char
            print(sum_char)
        else:
            print("Invalid indices!")


