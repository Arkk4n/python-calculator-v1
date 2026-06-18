import random

guess = 0
computer = random.randint(0, 100)

def set_difficulty():
  global guess
  difficulty = input("Choose your difficulty: ")
  if difficulty == "easy":
    guess = 10
  elif difficulty == "hard":
    guess = 5
  return guess

def check_answer():
  global computer
  global guess
  while guess > 0:
    player = int(input("Guess a number: "))
    if player == computer:
      print(computer)
      return f"You got it! The answer was {computer}."
    elif player > computer:
      guess -= 1
      print(f"Too high. Guess again. Guess left {guess}")
    else:
      guess -= 1
      print(f"Too low. Guess again. Guess left {guess}")
  return "You've run out of guesses, you lose."

set_difficulty()
check_answer()
