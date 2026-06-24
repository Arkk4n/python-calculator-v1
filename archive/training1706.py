def is_positive(number):
  if number > 0:
    return True
  else:
    return False

print(is_positive(-1))
print(is_positive(10))

numbers = [4, 7, 2, 9, 1, 15, 8]
largest = numbers[0]

for _ in numbers:
  if _ > largest:
    largest = _
    
print(largest)
    
lowest = numbers[0]
for _ in numbers:
  if _ < lowest:
    lowest = _
print(lowest)


def compare_numbers(a, b):
  if a > b:
    return "A is bigger"
  elif a < b:
    return "B is bigger"
  else:
    return "Equal"
  
print(compare_numbers(10, 5))
print(compare_numbers(5, 10))
print(compare_numbers(7, 7))

def compare_numbers2(a, b):
  difference = abs(a - b)
  return f"Difference is {difference}"

print(compare_numbers2(10, 5))
print(compare_numbers2(20, 8))