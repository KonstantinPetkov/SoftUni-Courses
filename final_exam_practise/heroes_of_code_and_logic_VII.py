def created_heroes(heroes_dict, number):
    for n in range(number):
        data = input().split(' ')
        hero_name, hit_points, mana_points = data[0], int(data[1]), int(data[2])
        heroes_dict[hero_name] = [hit_points, mana_points]


def play_game(heroes_dict):
    while True:
        command = input()
        if command == "End":
            break
        splited_command = command.split(' - ')
        current_command = splited_command[0]

        if current_command == 'CastSpell':
            hero_name, mp_needed, spell_name = splited_command[1], int(splited_command[2]), splited_command[3]
            mp_avaible = heroes_dict[hero_name][1]
            if mp_avaible >= mp_needed:
                heroes_dict[hero_name][1] -= mp_needed
                left_mp = heroes_dict[hero_name][1]
                print(f"{hero_name} has successfully cast {spell_name} and now has {left_mp} MP!")
            else:
                print(f"{hero_name} does not have enough MP to cast {spell_name}!")

        elif current_command == 'TakeDamage':
            hero_name, damage, attacker = splited_command[1], int(splited_command[2]), splited_command[3]
            avaible = heroes_dict[hero_name][0]
            if avaible - damage > 0:
                heroes_dict[hero_name][0] -= damage
                left_hp = heroes_dict[hero_name][0]
                print(f"{hero_name} was hit for {damage} HP by {attacker} and now has {left_hp} HP left!")
            else:
                del heroes_dict[hero_name]
                print(f"{hero_name} has been killed by {attacker}!")

        elif current_command == 'Recharge':
            hero_name, recharge_amount = splited_command[1], int(splited_command[2])
            mp_avaible = heroes_dict[hero_name][1]
            if mp_avaible + recharge_amount > 200:
                recharge_amount = 200 - mp_avaible
                heroes_dict[hero_name][1] += recharge_amount
            else:
                heroes_dict[hero_name][1] += recharge_amount
            print(f"{hero_name} recharged for {recharge_amount} MP!")

        elif current_command == 'Heal':
            hero_name, amount = splited_command[1], int(splited_command[2])
            hp_avaible = heroes_dict[hero_name][0]
            if hp_avaible + amount > 100:
                amount = 100 - hp_avaible
                heroes_dict[hero_name][0] += amount
            else:
                heroes_dict[hero_name][0] += amount
            print(f"{hero_name} healed for {amount} HP!")


number_of_heroes = int(input())
heroes_dict = {}
created_heroes(heroes_dict, number_of_heroes)
play_game(heroes_dict)
result = ''
for hero in heroes_dict:
    result += f'{hero}\n  HP: {heroes_dict[hero][0]}\n  MP: {heroes_dict[hero][1]}\n'
print(result)