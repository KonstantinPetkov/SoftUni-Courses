my_list = []
for i in range(3):
    command = input()
    my_list.append(command)

my_list[0], my_list[2] = my_list[2], my_list[0]
print(my_list)


