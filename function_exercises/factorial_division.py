def factorial(number):
    fact = 1
    for num in range(1, number + 1):
        fact *= num

    return fact


first_number = int(input())
second_number = int(input())
first_num_fact = factorial(first_number)
second_num_fact = factorial(second_number)
result = first_num_fact / second_num_fact
print(f"{result:.2f}")