numbers = [5, -2, 9, 0, 12, 3, -7]

# vytvor nový list:
# len kladné čísla menšie ako 10

new_numbers = []

for num in numbers:
  if num > 0 and num < 10:
    new_numbers.append(num)

print(new_numbers)  

player = {
    "name": "Tom",
    "health": 80,
    "inventory": ["sword", "potion"]
}

# vypíš:
# meno hráča
# počet itemov v inventory
# health po damage -30

print(player["name"])
print(len(player["inventory"]))
player["health"] -= 30
print(player["health"]) 

