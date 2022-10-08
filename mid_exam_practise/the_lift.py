people = int(input())
current_state_of_lift = list(map(int, input().split(" ")))

for element in range(len(current_state_of_lift)):
    sum_people = min(4 - current_state_of_lift[element], people)
    current_state_of_lift[element] += sum_people
    people -= sum_people

if people > 0:
    print(f"There isn't enough space! {people} people in a queue!")
elif len([lift for lift in current_state_of_lift if lift < 4]) > 0:
    print("The lift has empty spots!")

print(*current_state_of_lift, sep=" ")

