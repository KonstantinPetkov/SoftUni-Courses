number = int(input())

numbers = []

for i in range(number):
    current_number = int(input())
    numbers.append(current_number)

command = input()

filtered_numbers = []

for n in numbers:
    is_filtered = (
        (command == "even" and n % 2 == 0) or (command == "odd" and n % 2  != 0) or
        (command == "positive" and n >= 0) or (command == "negative" and n < 0)
    )
    if is_filtered:
        filtered_numbers.append(n)

print(filtered_numbers)
