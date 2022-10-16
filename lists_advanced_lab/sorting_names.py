names = input().split(', ')
sorted_name = sorted(names, key=lambda x: (-len(x), x))
print(sorted_name)