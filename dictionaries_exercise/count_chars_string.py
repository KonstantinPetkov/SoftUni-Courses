text = input().split()
symbols = ''.join(text)
letters = {}
for char in symbols:
    if char not in letters:
        letters[char] = 0
    letters[char] += 1
for key, value in letters.items():
    print(f"{key} -> {value}")

