import copy

cards_input = input().split()
shuffle_count = int(input())
half_deck = len(cards_input) // 2
top_card = cards_input[0]
bottom_card = cards_input[-1]
shuffle_cards = []

for shuffle in range(shuffle_count):
    left_side = []
    right_side = []

    for cards in range(1, half_deck):
        left_side.append(cards_input[cards])

    for cards in range(half_deck, len(cards_input) - 1):
        right_side.append(cards_input[cards])

    for shuffles in range(len(left_side)):
        shuffle_cards.append(right_side[shuffles])
        shuffle_cards.append(left_side[shuffles])

    cards_input = shuffle_cards.copy()
    cards_input.append(bottom_card)
    cards_input.insert(0, top_card)
    shuffle_cards = []

print(cards_input)
