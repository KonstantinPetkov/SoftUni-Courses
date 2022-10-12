def sum_numbers(first_num, second_num):
    return first_num + second_num

def subtract(sum_num, third_num):
    return sum_num - third_num

def add_and_subtract(first, second, third) :
    sum = sum_numbers(first, second)
    results = subtract(sum, third)
    return results

first_num = int(input())
second_num = int(input())
third_num = int(input())
print(add_and_subtract(first_num, second_num, third_num))