diviser = int(input())
boundary = int(input())
for n in range(boundary, diviser, -1):
    if n % diviser == 0:
        break
print(n)