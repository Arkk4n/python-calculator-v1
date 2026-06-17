
def check_winner(player_score, computer_score):
  if player_score > 21:
    return "Player Bust"
  elif computer_score > 21:
    return "Computer Bust"
  elif player_score > computer_score:
    return "Player Wins"
  elif computer_score > player_score:
    return "Computer Wins"
  else:
    return "Draw"
  
print(check_winner(25, 18))
print(check_winner(18, 25))
print(check_winner(20, 19))
print(check_winner(19, 20))
print(check_winner(20, 20))

def is_adult(age):
  if age >= 18:
    return True
  else:
    return False
    
print(is_adult(15))
print(is_adult(25))


password = "python123"
while True:
  guess = input("Guess a password: ")
  if guess == password:
    print("Acces granted.")
    break
  

import random

cards = [2, 3, 4, 5, 6, 7, 8, 9, 10]
player_cards = []

for _ in range(3):
  player_cards.append(random.choice(cards))
  
total = sum(player_cards)

print(f"Cards: {player_cards}")
print(f"Total: {total} ")
