import re

text = input()

pattern_of_hidden_word = r'([@#])([a-zA-Z]{3,})\1\1([a-zA-Z]{3,})\1'
matched_words = re.findall(pattern_of_hidden_word, text)
mirror_words = list()
valid_pairs_count = 0

for match in matched_words:
    valid_pairs_count += 1
    if match[1] == match[2][::-1]:
        mirror_words.append(f'{match[1]} <=> {match[2]}')

if matched_words:
    print(f"{valid_pairs_count} word pairs found!")
    if mirror_words:
        print("The mirror words are:")
        print(', '.join(mirror_words))
    else:
        print("No mirror words!")
else:
    print("No word pairs found!")
    print("No mirror words!")