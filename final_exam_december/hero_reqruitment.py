spell_book = {}

while True:
    command = input()
    if command == "End":
        break
    splitted_command = command.split()
    action = splitted_command[0]
    if action == "Enroll":
        hero_name = splitted_command[1]
        if hero_name not in spell_book.keys():
            spell_book[hero_name] = ''
        else:
            print(f"{hero_name} is already enrolled.")

    elif action == "Learn":
        hero_name = splitted_command[1]
        spell_name = splitted_command[2]
        if hero_name in spell_book.keys():
            if spell_name not in spell_book.values():
                spell_book[hero_name] = spell_name
            else:
                print(f"{hero_name} has already learnt {spell_name}.")
        else:
            print(f"{hero_name} doesn't exist.")

    elif action == "Unlearn":
        hero_name = splitted_command[1]
        spell_name = splitted_command[2]
        if hero_name in spell_book.keys():
            if spell_name in spell_book[hero_name]:
                for key, value in spell_book.items():
                    if value == spell_name:
                        spell_book[hero_name] = ''
            else:
                print(f"{hero_name} doesn't know {spell_name}.")
        else:
            print(f"{hero_name} doesn't exist.")

print("Heroes:")
for hero, spell in spell_book.items():
    print(f'== {hero}: {spell}')