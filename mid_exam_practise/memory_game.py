def check_indexes(indexes):
    if numbers[0] == numbers[1] or int(numbers[0]) >= len(sequence_of_elements) \
            or int(numbers[1]) >= len(sequence_of_elements) or int(numbers[0]) < 0 or int(numbers[1]) < 0:
        print("Invalid input! Adding additional elements to the board")
        sequence_of_elements.insert((len(sequence_of_elements) // 2), f'-{indexes}a')
        sequence_of_elements.insert((len(sequence_of_elements) // 2), f'-{indexes}a')
    else:
        return True

def check_elments(elements):
    first_elements = sequence_of_elements[int(numbers[0])]
    second_elements = sequence_of_elements[int(numbers[1])]
    if check_indexes(elements):
        if first_elements == second_elements:
            print(f"Congrats! You have found matching elements - {first_elements}!")
            for ch in sequence_of_elements:
                if ch == first_elements:
                    sequence_of_elements.remove(ch)
            if len(sequence_of_elements) == 0:
                check_winner(elements)
        else:
            print("Try again!")

def check_winner(elements):
    if len(sequence_of_elements) == 0:
        print(f"You have won in {elements} turns!")
    else:
        print("Sorry you lose :(")
        print(' '.join(sequence_of_elements))
    exit()


counter = 0
sequence_of_elements = input().split()
numbers = input().split()

while numbers[0] != 'end':
    counter += 1
    check_elments(counter)

    numbers = input().split()

check_winner(counter)




