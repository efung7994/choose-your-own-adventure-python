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

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line �
def game():
  path = input("There are two paths. Pick one. Left or Right? \n")
  if path.lower() == "right":
    gap = input("Oh no, there's a gap! Jump or Climb? \n")
    if gap.lower() == "climb":
      dragon = input("A dragon stands before you. Fight or Run? \n")
      if dragon.lower() == "fight":
        print("Ouch that hurts. Take this!")
        lawyer = input("The dragon punches you! Sue or Punch? \n")
        if lawyer.lower() == "sue":
          play_again = input("You sue the dragon and were entitled to 100 percent of its assets. Congrats! Play again? Y/N")
          if play_again.lower() == "y":
            game()
          else:
            print("Goodbye!")
        else:
          game_over = input("The dragon kills you. Try again? Y/N \n")
          if game_over.lower() == "y":
            game()
          else:
            print("Goodbye!")
      else:
        game_over = input("You ran into a wall and died. Try again? Y/N \n")
        if game_over.lower() == "y":
          game()
        else:
          print("Goodbye!")
    else:
      game_over = input("You jumped to your death. Try again? Y/N \n")
      if game_over.lower() == "y":
        game()
      else:
        print("Goodbye!")
  else:
    game_over = input("You took a wrong turn and died. Try again? Y/N \n")
    if game_over.lower() == "y":
      game()
    else:
      print("Goodbye!")

game()