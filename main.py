win = 100 
num = 1
temp = 0


le = True
while (le):
  if  num <= 100: 
    le = True
  else: 
    le = False

  user = int(input(""))
  if user < 2: 
    if user == 0: 
      le = False
      print("You Quit!")
    else: 
      print("Wrong input! Try again!")
      user = 0
  elif user > 12: 
    print("Wrong input! Try again!")
    user = 0
  else: 
    temp = user + num

  if temp == 100: 
    print("You win!")
    le = False
  else: 
    if temp > 100: 
      user = 0
      num += user
    else: 
      if temp == 54: 
        num = 19
      elif temp == 90: 
        num = 48
      elif temp == 99: 
        num = 77
      elif temp == 9:
        num = 34
      elif temp == 40: 
        num = 64
      elif temp == 67: 
        num = 86
      else: 
        num += user    
    print("You are on square {}".format(num))
