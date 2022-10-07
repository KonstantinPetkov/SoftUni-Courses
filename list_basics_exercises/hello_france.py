types = input().split("|")
budget = float(input())

bought_items_price = []
sold_items_price = []
for type in types:
    items = type.split("->")
    type_of_item = items[0]
    price_item = float(items[1])
    if type_of_item == "Clothes":
        if price_item <= 50.00 and budget >= price_item:
            bought_items_price.append(price_item)
            budget -= price_item
    elif type_of_item == "Shoes":
        if price_item <= 35.00 and budget >= price_item:
            bought_items_price.append(price_item)
            budget -= price_item
    elif type_of_item == "Accessories":
        if price_item <= 20.50 and budget >= price_item:
            bought_items_price.append(price_item)
            budget -= price_item
    else:
        continue

for element in bought_items_price:
    increased_element_value = element * 1.4
    sold_items_price.append(increased_element_value)
    budget += increased_element_value

sum_of_bought_items = sum(bought_items_price)
sum_of_sold_items = sum(sold_items_price)
profit = sum_of_sold_items - sum_of_bought_items
final_budget = budget + profit

formatted_list = ["%.2f" % elem for elem in sold_items_price]

print(*formatted_list)
print(f"Profit: {profit:.2f}")

if final_budget >= 150.00:
    print("Hello, France!")
else:
    print("Not enough money.")