import re

number = int(input())
pattern = r'(\!)([A-Z][a-z]{2,})(\!\:)(\[)([a-zA-Z]+)(\])'
matched_list = list()
ord_list = list()
for num in range(number):
    text = input()
    matched = re.search(pattern, text)
    if matched:
        string = matched.group(5)
        matched_list.append(string)
        for char in string:
            ord_char = ord(char)
            ord_list.append(str(ord_char))
        print(f"{matched.group(2)}: {' '.join(ord_list)}")
    else:
        print("The message is invalid")

