string = input()
res = [idx for idx in range(len(string)) if string[idx].isupper()]
print(res)