string = input()
counter = int(input())
result = lambda current_string, num: current_string * num
print(result(string, counter))