def subtract(a, b):
  return a - b

def divide(a, b):
  return a / b

def addition(a, b):
  return a + b

def multiplication(a, b):
  return a * b

def cont():
  user_answer = input("Do you want to continue? :")
  if user_answer == "y":
    return True
  else:
    return False
  
  
    

def calculator():  
  while True:
    first_number = int(input("Write first number: "))
    second_number = int(input("Write second number: "))
    
    operation = input("What calculation do you want to do: ")
    if operation == "+":
      print("Addition selected")
      result = addition(first_number, second_number)
    elif operation == "-":
      print("Substract selected")
      result = subtract(first_number, second_number)
    elif operation == "*":
      print("Multiplication selected")
      result = multiplication(first_number, second_number)
    elif operation == "/":
      print("Division selected")
      result = divide(first_number, second_number)
    print(result)
    if not cont():
      break
    

calculator()