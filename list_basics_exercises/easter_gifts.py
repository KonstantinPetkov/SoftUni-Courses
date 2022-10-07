gift_list = input().split()
command = input()
while command != "No Money":
    new_command = command.split()
    current_command = new_command[0]
    current_gift = new_command[1]
    if current_command == "OutOfStock":
        gift_list = [None if gift == current_gift else gift for gift in gift_list]
    elif current_command == "Required":
        new_gift_list = int(new_command[2])
        if 0 <= new_gift_list < len(gift_list):
            gift_list[new_gift_list] = current_gift
    elif current_command == "JustInCase":
        gift_list[-1] = current_gift
    command = input()

for elements in gift_list:
    if elements is not None:
        print(f"{elements}", end=" ")