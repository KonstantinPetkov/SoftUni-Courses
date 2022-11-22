text = input()
digits, letters, symbols = [], [], []

for char in text:
    if char.isdigit():
        digits.append(char)
    elif char.isalpha():
        letters.append(char)
    else:
        symbols.append(char)

print(''.join(digits))
print(''.join(letters))
print(''.join(symbols))
