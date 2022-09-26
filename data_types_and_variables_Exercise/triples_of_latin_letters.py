number_of_symbol = int(input())
for i in range(number_of_symbol):
    for j in range(number_of_symbol):
        for k in range(number_of_symbol):
            print(f"{chr(97 + i)}{chr(97 + j)}{chr(97 + k)}")
