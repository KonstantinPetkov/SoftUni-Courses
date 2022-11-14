orders = {}
products = input()
while products != "buy":
    current_product = products.split()
    name = current_product[0]
    price = float(current_product[1])
    quantity = int(current_product[2])

    if name not in orders.keys():
        orders[name] = [price, quantity]
    else:
        orders[name][1] += quantity
        if price != orders[name][0]:
            orders[name][0] = price

    products = input()

for product_name in orders:
    total_price = orders[product_name][0] * orders[product_name][1]
    print(f"{product_name} -> {total_price:.2f}")
