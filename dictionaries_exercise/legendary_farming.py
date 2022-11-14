items = {"shards" : 0, "fragments" : 0, "motes" : 0}
command = input().split()
obtained = False
while not obtained:
    for index in range(0, len(command), 2):
        value = int(command[index])
        key = command[index + 1].lower()
        if key not in items.keys():
            items[key] = 0
        items[key] += value
        if items["shards"] >= 250:
            print("Shadowmourne obtained!")
            items[key] -= 250
            obtained = True
        elif items["fragments"] >= 250:
            print("Valanyr obtained!")
            items[key] -= 250
            obtained = True
        elif items["motes"] >= 250:
            print("Dragonwrath obtained!")
            items[key] -= 250
            obtained = True
        if obtained:
            break
    if obtained:
        break

    command = input().split()

for material, quantity in items.items():
    print(f"{material}: {quantity}")