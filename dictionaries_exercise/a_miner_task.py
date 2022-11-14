resource = {}
while True:
    sequence_of_strings = input()
    if sequence_of_strings == "stop":
        break
    quantity = int(input())
    if sequence_of_strings not in resource:
        resource[sequence_of_strings] = 0
    resource[sequence_of_strings] += quantity
for key, value in resource.items():
    print(f"{key} -> {value}")


