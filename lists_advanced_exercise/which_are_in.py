first_sequences = input().split(', ')
second_sequences = input().split(', ')
result = []
for first_word in first_sequences:
    for second_word in second_sequences:
        if first_word in second_word:
            result.append(first_word)
            break
print(result)