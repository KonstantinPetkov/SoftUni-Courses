def average_number(numbers):
    average = 0
    for num in range(len(numbers)):
        average += numbers[num]

    average = average // len(numbers)
    list_of_numbers = []
    for value in range(len(numbers)):
        if numbers[value] > average:
            list_of_numbers.append(str(numbers[value]))

    if sum(numbers) < 0:
        return list_of_numbers[-5:]
    else:
        sorted_numbers = sorted(list_of_numbers, reverse=True)
        return sorted_numbers[:5]


sequence_of_numbers = list(map(int, input().split()))
result = average_number(sequence_of_numbers)
if len(sequence_of_numbers) <= 1:
    print("No")
else:
    print(" ".join(result))
