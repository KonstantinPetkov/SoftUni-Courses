def calculates(type_of_product, num):
    if type_of_product == "coffee":
        return num * 1.50
    elif type_of_product == "coke":
        return num * 1.40
    elif type_of_product == "water":
        return num * 1.00
    elif type_of_product == "snacks":
        return num * 2.00

product = input()
quantity = int(input())
format_float = "{:.2f}".format(calculates(product, quantity))
print(format_float)