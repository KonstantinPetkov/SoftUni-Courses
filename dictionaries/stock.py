items = input().split()
searched_product = input().split()
my_dictionary = {}
for index in range(0, len(items), 2):
    key = items[index]
    value  = int(items[index + 1])
    my_dictionary[key] = value
for product in searched_product:
    if product in my_dictionary.keys():
        quantity = my_dictionary[product]
        print(f"We have {quantity} of {product} left")
    else:
        print(f"Sorry, we don't have {product}")






