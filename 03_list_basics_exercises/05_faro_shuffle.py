card_deck = input().split()
shuffle_count = int(input())

for current_shuffle in range(shuffle_count):
    middle_deck = len(card_deck) // 2

    left_part = card_deck[:middle_deck]
    right_part = card_deck[middle_deck:]

    deck_after_shuffle = []

    for card_index in range(len(right_part)):
        deck_after_shuffle.append(left_part[card_index])
        deck_after_shuffle.append(right_part[card_index])
    card_deck = deck_after_shuffle.copy()

print(card_deck)