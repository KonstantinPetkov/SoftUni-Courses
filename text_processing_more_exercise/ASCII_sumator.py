first_char = input()
second_char = input()
text = input()
result = 0
for char in text:
    if ord(first_char) < ord(char) < ord(second_char):
        result += ord(char)
print(result)