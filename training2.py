users = {
    "tom": [10, 20],
    "anna": [5, 15, 10],
    "john": [30]
}

highest_score = 0
best_user = ""

for user, scores in users.items():
  current_score = max(scores)
  if current_score > highest_score:
    highest_score = current_score
    best_user = user
    
print(f"Best player: {best_user}")
print(f"Highest score: {highest_score}")