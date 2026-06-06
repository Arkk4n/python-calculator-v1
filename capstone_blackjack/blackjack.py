import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

player_cards = []


computer_cards = []

for _ in range(2):
    player_cards.append(random.choice(cards))
    computer_cards.append(random.choice(cards))
print(player_cards)
print(computer_cards)



def calculate_score(cards):
    return sum(cards)


player_score = calculate_score(player_cards)
computer_score = calculate_score(computer_cards)
print(player_score)
print(computer_score)

