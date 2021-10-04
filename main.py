print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

choice = input('''There's a maze in front of you. Which way do you want to go?
Type 'left' or 'right' to progress. ''')
pilihan = choice.lower()
if pilihan == "right" :
  print("You are bitten to the death by magical beast.")
elif pilihan == "left" :
  choice = input('''You walk out from the maze, then there's is a lake in front of you. What would you do? \nType 'swim' or 'wait' to progress. ''')
  pilihan = choice.lower()
  if pilihan == "swim" :
    print("You got eaten by crocodiles!")
  elif pilihan == "wait" :
    choice = input('''You got across of the lake. Then there are 3 doors in front of you.\nWhich door would you like to got in? Red, orange, yellow, or green?\nType 'red', 'orange', 'yellow', or 'green' to progress. ''')
    pilihan = choice.lower()
    if pilihan == "red" :
      print("You got burned by the flamethrower when you open the door.")
    elif pilihan == "orange" :
      print("You got crushed by a bunch of oranges.")
    elif pilihan == "yellow" :
      print("You found the treasure. Congratulations!")
    elif pilihan == "green" :
      print("A bunch of trees fall upon your head. You died.")
  

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload