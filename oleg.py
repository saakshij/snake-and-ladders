done = False
endMessage = "You Quit!"
currentSpace = 1

while not done:
  toMove = int(input())
  if toMove == 0:
    done = True
    break
  currentSpace += toMove
  if currentSpace == 9:
    currentSpace = 34
  elif currentSpace == 40:
    currentSpace = 64
  elif currentSpace == 54:
    currentSpace = 19
  elif currentSpace == 67:
    currentSpace = 86
  elif currentSpace == 90:
    currentSpace = 48
  elif currentSpace == 99:
    currentSpace = 77
  if currentSpace > 100:
    currentSpace -= toMove
  print("You are now on square " + str(currentSpace))
  if currentSpace == 100:
    endMessage = "You Win!"
    done = True

print(endMessage)
