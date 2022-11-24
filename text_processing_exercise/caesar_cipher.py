first_massage = input()
second_message = ''
for char in first_massage:
    new_symbol = chr(ord(char) + 3)
    second_message += new_symbol
print(second_message)