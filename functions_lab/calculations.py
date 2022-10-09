def calculates(a, b, operator):
    if operator == "multiply":
        return a * b
    elif operator == "divide":
        return int(a / b)
    elif operator == "add":
        return a + b
    elif operator == "subtract":
        return a - b

operator = input()
first_number = int(input())
second_number = int(input())

print(calculates(first_number, second_number, operator))