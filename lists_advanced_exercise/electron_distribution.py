number = int(input())
filled_shells = []
counter = 0
for num in range(number):
    if number <= 0:
        break
    counter += 1
    current_shell = 2 * counter ** 2
    if number >= current_shell:
        filled_shells.append(current_shell)
        number -= current_shell
    else:
        filled_shells.append(number)
        break

print(filled_shells)
