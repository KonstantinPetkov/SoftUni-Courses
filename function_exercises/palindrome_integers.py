def palindrome(element):
    for element in list_number:
        if element == element[::-1]:
            print(True)
        else:
            print(False)


list_number = input().split(", ")
palindrome(list_number)
