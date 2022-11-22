initial_number = int(input())
pieces_dict = {}

for num in range(initial_number):
    piece, composer, key = input().split("|")
    if piece not in pieces_dict.keys():
        pieces_dict[piece] = pieces_dict.get(piece, {})
    pieces_dict[piece][composer] = key

while True:
    command = input()
    if command == "Stop":
        break
    splited_command = command.split("|")
    action = splited_command[0]
    if action == "Add":
        piece_name = splited_command[1]
        composer_name = splited_command[2]
        key_name = splited_command[3]
        if piece_name in pieces_dict.keys():
            if composer_name not in pieces_dict.values():
                print(f"{piece_name} is already in the collection!")
        if piece_name not in pieces_dict.keys():
            pieces_dict[piece_name] = pieces_dict.get(piece_name, {})
            pieces_dict[piece_name][composer_name] = key_name
            if composer_name not in pieces_dict.values():
                print(f"{piece_name} by {composer_name} in {key_name} added to the collection!")
    elif action == "Remove":
        remove_name = splited_command[1]
        if remove_name in pieces_dict.keys():
            del pieces_dict[remove_name]
            print(f"Successfully removed {remove_name}!")
        else:
            print(f"Invalid operation! {remove_name} does not exist in the collection.")

    elif action == "ChangeKey":
        change_name = splited_command[1]
        new_key_name = splited_command[2]
        if change_name in pieces_dict.keys():
            item, name_compositor = pieces_dict[change_name].popitem()
            pieces_dict[change_name] = {}
            pieces_dict[change_name][composer_name] = new_key_name
            print(f"Changed the key of {change_name} to {new_key_name}!")
        else:
            print(f"Invalid operation! {change_name} does not exist in the collection.")


for name in pieces_dict:
    for new_key_name, name_compositor in pieces_dict[name].items():
        print(f"{name} -> Composer: {new_key_name}, Key: {name_compositor}")
