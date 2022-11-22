number = int(input())
plants_dict = {}

for num in range(number):
    plant, rarity = input().split("<->")
    if plant not in plants_dict.keys():
        plants_dict[plant] = {}
    plants_dict[plant]["rarity"] = float(rarity)
    plants_dict[plant]["rating"] = []


def check_plant(name):
    if name not in plants_dict.keys():
        print("error")
        return
    return True


def rated_plant(rated_plant, new_rating):
    if check_plant(rated_plant):
        plants_dict[rated_plant]["rating"].append(new_rating)


def update_plant(updated_plant, new_rarity):
    if check_plant(updated_plant):
        plants_dict[updated_plant]["rarity"] = new_rarity


def reset_plant(reseted_plant):
    if check_plant(reseted_plant):
        plants_dict[reseted_plant]["rating"] = []


while True:
    command = input()
    if command == "Exhibition":
        break
    splited_command = command.split(": ")
    action = splited_command[0]
    new_plant = splited_command[1]
    new_splited_command = new_plant.split(" - ")
    if action == "Reset":
        reset_plant(new_plant)
        continue
    elif action == "Rate":
        rated_plant(new_splited_command[0], float(new_splited_command[1]))
    elif action == "Update":
        update_plant(new_splited_command[0], float(new_splited_command[1]))

print("Plants for the exhibition:")

for name in plants_dict.keys():
    avg = 0
    if sum(plants_dict[name]["rating"]) != 0:
        avg = sum(plants_dict[name]["rating"]) / len(plants_dict[name]["rating"])
    print(f"- {name}; Rarity: {plants_dict[name]['rarity']:.0f}; Rating: {avg:.2f}")