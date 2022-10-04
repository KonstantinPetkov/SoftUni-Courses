money_list = input().split(", ")
number_baggers = int(input())

final_money_list = []
money_list_as_digit = []
starting_index = 0
for element in money_list:
    money_list_as_digit.append(int(element))

while starting_index < number_baggers:
    sum_current_beggar = 0
    for i in range(starting_index, len(money_list_as_digit), number_baggers):
        sum_current_beggar += money_list_as_digit[i]
    final_money_list.append(sum_current_beggar)
    starting_index += 1

print(final_money_list)