def collect_char(first, second):
    charecter = []
    for current_char in range(ord(first) + 1, ord(second)):
        charecter.append(chr(current_char))
    return charecter

first_char = input()
second_char = input()
results = collect_char(first_char, second_char)
#print(*results, sep=" ")
print(' '.join(results))