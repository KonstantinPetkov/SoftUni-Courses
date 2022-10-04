list_of_number = input().split(" ")
delete_number = int(input())
final_list = []
for element in list_of_number:
    final_list.append(int(element))
for digit in range(delete_number):
    final_list.remove(min(final_list))

print(*final_list, sep = ", ")
