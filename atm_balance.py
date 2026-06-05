

balance = 100

while True:
  
  user_input = input("Write your command: ").lower()
  if user_input == "balance":
    print(balance)
  elif user_input == "deposit":
    user_deposit = int(input("How much do you want deposit?: "))
    balance += user_deposit
  elif user_input == "withdraw":
    user_withdraw = int(input("How much do you want to withdraw?: "))
    balance -= user_withdraw
  elif user_input == "quit":
    break
  
