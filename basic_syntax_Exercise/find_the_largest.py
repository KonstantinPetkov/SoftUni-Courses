num = int(input())
num_str = str(num)
print(int(''.join(sorted(num_str, reverse=True))))
