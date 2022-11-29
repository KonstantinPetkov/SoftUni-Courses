import re

furniture = []
total_cost = 0
pattern = r'>>([a-zA-z]+)<<(\d+\.?\d*)!(\d+)'
while True:
    command = input()
    if command == "Purchase":
        break
    match = re.search(pattern, command)
    if match:
        furniture_name, price, quantity = match.groups()
        furniture.append(furniture_name)
        total_cost += float(price) * int(quantity)

print("Bought furniture:")
for item in furniture:
    print(item)
print(f"Total money spend: {total_cost:.2f}")