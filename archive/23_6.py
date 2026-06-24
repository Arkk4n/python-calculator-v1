def is_even(number):
  if number % 2 == 0:
    return True
  else:
    return False

  
print(is_even(4))
print(is_even(7))
print(is_even(10))

numbers = [3, 8, 2, 15, 7]
summary = 0
for _ in numbers:
  summary += _

print(summary)
  
def countdown(number):
  while number > 0:
    print(number)
    number -= 1

countdown(5)
