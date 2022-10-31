secret_message = input().split()
letters = []
digits = []
for element in secret_message:
    number = ""
    letter = ""
    for symbol in element:
        if symbol.isdigit():
            number += symbol
        else:
            letter += symbol
    digits.append(int(number))
    if len(letter) > 1:
        letter = f"{letter[-1]}{letter[1:-1]}{letter[0]}"
    letters.append(letter)

for num, word in zip(digits, letters):
    print(f"{chr(num)}{word}", end=" ")
