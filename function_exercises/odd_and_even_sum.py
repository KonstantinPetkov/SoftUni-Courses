def even_and_odd(number):
    sum_of_odd_digits = 0
    sum_of_even_digits = 0
    for element in number:
        if int(element) % 2 == 0:
            sum_of_even_digits += int(element)
        else:
            sum_of_odd_digits += int(element)
    return sum_of_odd_digits, sum_of_even_digits


number_as_string = input()
sum_of_odd_digits, sum_of_even_digits = even_and_odd(number_as_string)
print(f"Odd sum = {sum_of_odd_digits}, Even sum = {sum_of_even_digits}")