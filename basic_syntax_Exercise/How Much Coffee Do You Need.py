command = input()
total_of_coffee = 0
enough_coffee = True
while command != "END":
    if total_of_coffee == 5:
        enough_coffee = False
        break
    if command == "coding":
        total_of_coffee += 1
    elif command == "CODING":
        total_of_coffee += 2
    elif command == "dog" or command == "cat":
        total_of_coffee += 1
    elif command == "DOG" or command == "CAT":
        total_of_coffee += 2
    elif command == "movie":
        total_of_coffee += 1
    elif command == "MOVIE":
        total_of_coffee += 2
    else:
        pass
    command = input()

if enough_coffee:
    print(total_of_coffee)
else:
    print("You need extra sleep")