list_of_characters = input().split(", ")
dictionary = {char:ord(char) for char in list_of_characters}
print(dictionary)