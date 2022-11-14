phonebook = {}

while True:
    data = input()
    if "-" not in data:
        break
    name, number = data.split("-")
    phonebook[name] = number

for element in range(int(data)):
    searched_name = input()
    if searched_name in phonebook.keys():
        print(f"{searched_name} -> {phonebook[searched_name]}")
    else:
        print(f"Contact {searched_name} does not exist.")
