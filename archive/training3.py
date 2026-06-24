def multiply(a, b):
  return a * b

print(multiply(5, 2))

player = {
    "name": "Tom",
    "coins": 150
}

player["coins"] -= 30
print(player["coins"])
  
  
numbers = [5, 12, 3, 20, 8]
highest = 0

for num in numbers:
  if num > highest:
    highest = num

print(highest)