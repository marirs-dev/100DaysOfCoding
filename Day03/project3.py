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

# https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

input1 = input("You are at the cross road. Where do you want to go? Type 'left' or 'right' \n").lower()
if input1 == "left":
    input2 = input(
        "You came to lake. There is an island in the middle of the lake. Type 'wait' to wait for boat. Type 'swim' to "
        "swim across \n").lower()
    if input2 == "wait":
        input3 = input("You arrive at the island unharmed. There is house with 3 doors. One red, one blue and one "
                       "yellow. Which color do you choose? \n").lower()
        if input3 == "red":
            print("You burned by fire.")
            print("Game Over")
        elif input3 == "blue":
            print("You eaten by beasts.")
            print("Game Over")
        elif input3 == "yellow":
            print("You Win!")
        else:
            print("Game Over")
    else:
        print("You are attacked by trout.")
        print("Game Over")
else:
    print("Fall into a hole.")
    print("Game Over")
