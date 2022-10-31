days = int(input())
players = int(input())
group_energy = float(input())
water_for_person_per_day = float(input())
food_for_person_per_day = float(input())
total_water = water_for_person_per_day * players * days
total_food = food_for_person_per_day * players * days

for day in range(1, days + 1):
    amount_of_energy_loss = float(input())
    group_energy -= amount_of_energy_loss
    if group_energy <= 0:
        break
    if day % 2 == 0:
        group_energy *= 1.05
        total_water *= 0.7
    if day % 3 == 0:
        total_food = total_food - (total_food / players)
        group_energy *= 1.1

if group_energy > 0:
    print(f"You are ready for the quest. You will be left with - {group_energy:.2f} energy!")
else:
    print(f"You will run out of energy. You will be left with {total_food:.2f} food and {total_water:.2f} water.")