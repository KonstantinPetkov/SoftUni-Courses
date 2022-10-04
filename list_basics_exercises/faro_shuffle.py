deck = input().split()
number_shuffles = int(input())

for shuffle in range(number_shuffles):
    final_deck = []
    middle_of_deck = len(deck) // 2
    left_side = deck[0: middle_of_deck]
    right_side = deck[middle_of_deck::]
    for card_index in range(len(left_side)):
        final_deck.append(left_side[card_index])
        final_deck.append(right_side[card_index])
    deck = final_deck

print(final_deck)