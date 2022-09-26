budget = float(input())
price_of_one_kg_flour = float(input())

bread_counter = 0
collored_eggs_counter = 0
price_of_eggs = price_of_one_kg_flour * 0.75
price_of_milk = price_of_one_kg_flour * 1.25 / 4
price_of_one_bread = price_of_one_kg_flour + price_of_eggs + price_of_milk

while budget >= price_of_one_bread:
    budget -= price_of_one_bread
    bread_counter += 1
    collored_eggs_counter += 3
    if bread_counter % 3 == 0:
        collored_eggs_counter -= bread_counter -2

print(f"You made {bread_counter} loaves of Easter bread! Now you have {collored_eggs_counter} eggs and {budget:.2f}BGN left.")