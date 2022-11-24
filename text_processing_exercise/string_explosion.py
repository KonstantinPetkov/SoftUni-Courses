text = input()
new_text = ''
strength = 0
for index in range(len(text)):
    if strength > 0 and text[index] != ">":
        strength -= 1
    elif text[index] == ">":
        new_text += text[index]
        strength += int(text[index + 1])
    else:
        new_text += text[index]
print(new_text)