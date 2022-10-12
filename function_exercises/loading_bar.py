def loading_bar(current_number):
    if current_number == 100:
        return "100% Complete!\n[%%%%%%%%%%]"
    return f"{current_number}% [{'%' * (current_number // 10)}{'.' * (10 - (current_number // 10))}]\nStill loading..."


number = int(input())
print(loading_bar(number))