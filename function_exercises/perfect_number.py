def perfect_number(some_number):
    sum = 0
    for num in range(1, some_number):
        if some_number % num == 0:
           sum += num
    if sum == some_number:
        return "We have a perfect number!"
    else:
        return "It's not so perfect."


number = int(input())
print(perfect_number(number))