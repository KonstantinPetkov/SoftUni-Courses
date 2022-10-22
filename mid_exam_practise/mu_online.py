dungeon_rooms = input().split("|")
health = 100
bitcoins = 0
counter_of_room = 0
is_alive = True
for room in dungeon_rooms:
    command = room.split()
    current_command = command[0]
    number = int(command[1])
    counter_of_room += 1
    if current_command == "potion":
        current_health = health
        health += number
        if health >= 100:
            health = 100
        amount = health - current_health
        print(f"You healed for {amount} hp.")
        print(f"Current health: {health} hp.")
    elif current_command == "chest":
        bitcoins += number
        print(f"You found {number} bitcoins.")
    else:
        health -= number
        if not health <= 0:
            print(f"You slayed {current_command}.")
        else:
            print(f"You died! Killed by {current_command}.")
            print(f"Best room: {counter_of_room}")
            is_alive = False
            break

if is_alive:
    print("You've made it!")
    print(f"Bitcoins: {bitcoins}")
    print(f"Health: {health}")
