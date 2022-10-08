target = [int(n) for n in input().split()]
command = input()
shots = 0
while command != "End":
    current_index = int(command)
    if 0 <= current_index <= len(target) - 1 and target[current_index] != -1:
        shots += 1
        target_value = target[current_index]
        for index, value in enumerate(target):
            if value != -1:
                results = value - target_value
                if value <= target_value:
                    results = value + target_value
                target[index] = results
        target[current_index] = -1

    command = input()

print(f"Shot targets: {shots} ->", *target, sep=" ")