import re

products = []
total_income = 0
pattern = r'(%)([A-Z][a-z]+)\1([^\|\$\%\.]*)\<([\w]+)\>([^\|\$\%\.]*)\|([\d]+)\|([^\|\$\%\.]*)([1-9]+[.\d]*)\$'
while True:
    command = input()
    if command == "end of shift":
        break
    matched = re.search(pattern, command)
    if matched:
        count = matched.group(6)
        price = matched.group(8)
        total_price = float(count) * float(price)
        total_income += total_price
        print(f"{matched.group(2)}: {matched.group(4)} - {total_price:.2f}")

print(f"Total income: {total_income:.2f}")









