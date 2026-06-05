def check_number(number):
  if number % 2 == 0:
    return "Even"
  else:
    return "Odd"
  
print(check_number(2))
player = {
    "name": "Tom",
    "health": 70,
    "gold": 100
}

player["gold"] -= 40
player["health"] += 20

print(player["gold"], player["health"])

numbers = [4, 18, 2, 33, 21, 9]
lowest_numb = numbers[0]
for num in numbers:
  if num < lowest_numb:
    lowest_numb = num

print(lowest_numb)