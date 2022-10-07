initial_energy = int(input())
command = input()
battle = 0
energy = initial_energy
while command != "End of battle":
    distance = int(command)
    if battle % 3 == 0:
        energy += battle
    if energy >= distance:
        energy -= distance
    else:
        break
    battle += 1

    command = input()

if command == "End of battle":
    print(f"Won battles: {battle}. Energy left: {energy}")
else:
    print(f"Not enough energy! Game ends with {battle} won battles and {energy} energy")