version = input().split('.')
converted_version = [int(number) for  number in version]
converted_version[-1] += 1
for index in range(len(converted_version) - 1, -1, -1):
    if converted_version[index] > 9:
        converted_version[index] = 0
        if index - 1 >= 0:
            converted_version[index - 1] += 1
print('.'.join(str(number) for number in converted_version))
