def reduce(targets_sequence, index):
    special_value = targets_sequence[index]
    targets_sequence[index] = -1

    for i in range(len(targets_sequence)):
        if targets_sequence[i] == -1:
            continue

        if special_value < targets_sequence[i]:
            targets_sequence[i] -= special_value
        else:
            targets_sequence[i] += special_value

    return targets_sequence


def shoot(targets_sequence):
    counter = 0

    command = input()
    while command != "End":
        index = int(command)
        if 0 <= index < len(targets) and targets_sequence[index] != -1:
            counter += 1
            reduce(targets_sequence, index)

        command = input()


    print(f"Shot targets: {counter} -> {' '.join(map(str, targets))}")

targets = list(map(int, input().split()))
shoot(targets)
