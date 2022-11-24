text = input()
final_text = ''
last_letter = ''
for letter in text:
    if letter != last_letter:
        final_text += letter
        last_letter = letter
print(final_text)