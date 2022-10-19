numbers = list(map(int, input().split(", ")))
for num in range(1, 10 + 1):
    list_of_numbers = []
    if len(numbers) > 0:
        for add_num in numbers:
            if add_num <= (num * 10):
                list_of_numbers.append(add_num)
        for remove_num in list_of_numbers:
            numbers.remove(remove_num)

        print(f"Group of {num * 10}'s: {list_of_numbers}")
