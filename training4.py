def check_energy(energy):
  if energy > 50:
    return "High energy"
  elif energy > 20:
    return "Medium energy"
  else:
    return "Low energy"
  

print(check_energy(10))


numbers = [3, 8, 12, 1, 15, 6]
new_numbers = []

for num in numbers:
  if num > 5 and num % 2 == 0:
    new_numbers.append(num)
  
print(new_numbers)

player = {
    "name": "Tom",
    "health": 100,
    "inventory": ["potion", "sword"]
}

player["health"] += 20
player["inventory"].remove("potion")
print(player["health"], player["inventory"])


players = {
    "Tom": 45,
    "Anna": 78,
    "John": 62,
    "Mike": 90
}
highest_score = 0
best_player = ""
for player, score in players.items():
  if score > highest_score:
    highest_score = score
    best_player = player
  
print(f"Highest score is {highest_score} and player {best_player}")
