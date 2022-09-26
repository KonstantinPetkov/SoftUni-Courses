name = input()
welcome = True
while name != "Welcome!":
    if len(name) < 5:
        print(f"{name} goes to Gryffindor.")
    elif len(name) == 5:
        print(f"{name} goes to Slytherin.")
    elif len(name) == 6:
        print(f"{name} goes to Ravenclaw.")
    elif len(name) > 6 and name != "Voldemort":
        print(f"{name} goes to Hufflepuff.")
    elif name == "Voldemort":
        print("You must not speak of that name!")
        welcome = False
        break
    name = input()
if welcome:
    print("Welcome to Hogwarts.")


