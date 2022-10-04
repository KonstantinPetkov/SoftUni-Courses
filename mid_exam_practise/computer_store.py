command = input()
price_without_tax = 0
tax = 0
final_price = 0

while command != "special" and command != "regular":
    current_price = float(command)
    if current_price <= 0:
        print("Invalid price!")
        command = input()
        continue
    price_without_tax += current_price

    command = input()

tax = (price_without_tax * 1.20) - price_without_tax
final_price = price_without_tax + tax

if command == "special":
    final_price *= 0.9

if final_price == 0:
    print("Invalid order!")
else:
    print("Congratulations you've just bought a new computer!")
    print(f"Price without taxes: {price_without_tax:.2f}$")
    print(f"Taxes: {tax:.2f}$")
    print("-----------")
    print(f"Total price: {final_price:.2f}$")






