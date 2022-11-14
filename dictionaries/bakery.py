products = input().split()
my_dictionary = {}
for index in range(0, len(products), 2):
    food, quantities  = products[index], int(products[index + 1])
    my_dictionary[food] = quantities
print(my_dictionary)













