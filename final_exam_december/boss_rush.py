import re

number = int(input())
for n in range(number):
    text = input()
    pattern = r'\|([A-Z]{4,})\|:#([a-zA-Z]+[\s][a-zA-Z]+)#'
    valid = re.search(pattern, text)
    if valid:
        print(f"{valid.group(1)}, The {valid.group(2)}")
        print(f'>> Strength: {len(valid.group(1))}')
        print(f'>> Armor: {len(valid.group(2))}')
    else:
        print("Access denied!")