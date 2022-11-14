number = int(input())
dictionary = {}
for num in range(number):
    word = input()
    synonym = input()
    if word not in dictionary:
        dictionary[word] = []
    dictionary[word].append(synonym)
for word in dictionary:
    print(f"{word} - {', '.join(dictionary[word])}")