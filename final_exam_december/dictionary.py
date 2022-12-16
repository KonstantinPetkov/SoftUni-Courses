notebook_dict = {}

input_string = input().split(" | ")
for element in input_string:
    splited_element = element.split(": ")
    for index in range(0, len(splited_element), 2):
        key, value = splited_element[index], splited_element[index + 1]
        notebook_dict[key] = notebook_dict.get(key, [])
        notebook_dict[key].append(value)

words = input().split(" | ")
command = input()
for word in words:
    if command == "Test":
        if word in notebook_dict.keys():
            print(f"{word}:")
            for value in notebook_dict[word]:
                print(f" -{value}")

if command == "Hand Over":
    print(' '.join(notebook_dict.keys()))

