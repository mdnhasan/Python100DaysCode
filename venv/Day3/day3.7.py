##Project Treasure Hunt

print(''' ******************************************************************************
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
*******************************************************************************''')


print("Welcome to Hunt")
print("Your mission is to find treasure")
path = input('You\'re at a cross road.Where do you want to go? Type"Left" or "right"\n')
low_path=path.lower()

if low_path=='left':
    newpath=input('You came to a lake.The lake is in middle of island.Type "wait" for boat.Type "swim to swim to swim accross\n')
    low_newpath=newpath.lower()
    if low_newpath=='wait':
        destination= input("You came to island safely. There is a house with 3 doors. Red,Yellow,Blue. Which you choose\n")
        low_dest= destination.lower()
        if low_dest=='red' or low_dest=='blue':
            print("Game Over")
        elif low_dest=='yellow':
            print("You win")
        else:
            print("Invalid Choice")
    else:
        print("Game Over")
else:
    print("Game Over")
