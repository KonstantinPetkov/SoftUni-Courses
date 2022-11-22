dwarf_data = {}
hat = ""
name_hat = ""
physics = ""
name_of_item = ""
result = []
while True:
    dwarf = input()
    if dwarf == "Once upon a time":
        break
    new_dwarf = dwarf.split(" <:> ")
    dwarf_name = new_dwarf[0]
    dwarf_hat_color = new_dwarf[1]
    dwarf_physics = int(new_dwarf[-1])
    if dwarf_hat_color not in dwarf_data.keys():
        dwarf_data[dwarf_hat_color] = {}
    if dwarf_name not in dwarf_data[dwarf_hat_color].keys():
        dwarf_data[dwarf_hat_color][dwarf_name] = 0
    if dwarf_data[dwarf_hat_color][dwarf_name] < dwarf_physics:
        dwarf_data[dwarf_hat_color][dwarf_name] = dwarf_physics

for item_name in dwarf_data:
    for name, physic in dwarf_data[item_name].items():
        result.append({hat: len(dwarf_data[item_name]), name_hat: name, physics: physic, name_of_item: item_name})
for snow in sorted(result, key=lambda item: (-item[physics], -item[hat])):
    print(f"({snow[name]}) {snow[name_hat]} <-> {snow[physics]}")

