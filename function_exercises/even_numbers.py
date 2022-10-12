def check_even(number):
    if number % 2 == 0:
        return True
    return False

list_of_numbers = list(map(int, input().split(" ")))
result = filter(check_even, list_of_numbers)
even_numbers = list(result)

print(even_numbers)