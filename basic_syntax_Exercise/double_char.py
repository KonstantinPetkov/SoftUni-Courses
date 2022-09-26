string = input()
while string != "End":
    if string == "SoftUni":
        pass
    else:
        for char in string:
            print(char * 2, end="")
        print()

    string = input()

