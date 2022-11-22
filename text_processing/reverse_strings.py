text = input()
while text != "end":
    reversed_word = text[::-1]
    print(f"{text} = {reversed_word}")
    text = input()
