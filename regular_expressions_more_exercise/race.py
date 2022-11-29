import re

participants = input().split(", ")
list_of_participants = {name: 0 for name in participants}
distance = 0
pattern_letters = r'[A-Za-z]'
pattern_digits = r'[0-9]'
while True:
    command = input()
    if command == "end of race":
        break
    match_names = ''.join(re.findall(pattern_letters, command))
    match_digits = re.findall(pattern_digits, command)
    sum_of_numbers = sum(int(num) for num in match_digits)
    if match_names in list_of_participants.keys():
        list_of_participants[match_names] += sum_of_numbers

sorted_dict = sorted(list_of_participants.items(), key=lambda x: -x[1])

print(f"1st place: {sorted_dict[0][0]}")
print(f"2nd place: {sorted_dict[1][0]}")
print(f"3rd place: {sorted_dict[2][0]}")




