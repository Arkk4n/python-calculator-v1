import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

player_cards = []


computer_cards = []

for _ in range(2):
    player_cards.append(random.choice(cards))
    computer_cards.append(random.choice(cards))

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    elif 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)
player_score = calculate_score(player_cards)
computer_score = calculate_score(computer_cards)

if player_score == 0:
    print("Blackjack!")
else:
    while True:
        another_card = input("Do you want another card? y/n:")
        if another_card == "y":
            player_cards.append(random.choice(cards))
            player_score = calculate_score(player_cards)
            print(f"Your cards: {player_cards}")
            print(f"Your score: {player_score}")
        if another_card == "n":
            break
        if player_score > 21:
            print("Bust!")
            break

















