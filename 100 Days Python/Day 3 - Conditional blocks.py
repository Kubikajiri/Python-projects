# If Else
import sys

print("Welcome to the rollercoaster!")
height = int(input("What's your height young man?\n"))

if height > 120:
    print("Enjoy the ride!")
    age = int(input("How old are you young man/women?\n"))
    if age < 12:
        bill = 5
    elif 12 < age < 18:
        bill = 7
    elif 45 < age < 55:
        bill = 0
        print("Everything is fine, you ride for free ;P")
    else:
        bill = 12
    photos = input("Do you want photos? y/n\n")
    if photos == 'y':
        bill_with_photo = bill + 3
        print(f"the total bill is {bill_with_photo} $")
    else:
        print(f"the total bill is {bill} $")
else:
    print("sorry, you have to grow taller :(")

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

#Write your code below this line 👇

left_right = input("You're at the crossroads. The road to the left leads to a hill but you can't see what's above it. On the right you see a nice tree. Choose left or right\n")

if left_right == "left":
    wait_swim = input("You approach to a shore. Do you wait for a boat or you try your luck in swimming? The boat may never arrive and you may starve. ")
else:
    print("You fall into a hole and you die. RIP")
    sys.exit()
if wait_swim == "wait":
    doors = input("Your patience is rewarded! The boat arrived and you safetly got on a second island. After you've reached the shore you see 3 doors: Red, Yellow and Blue. Which one?\n")
else:
    print("Even if you thought you are strong enought to reach the shore, the tides prove you otherwise. The ocean depths claimed you as you will forever be part of the waters.Game over\n")
if doors == "Red" or doors == "red":
    print("You've fallen in the fire pit. The island tribe has given you to the gods and you burned alive.")
elif doors == "Yellow" or doors == "yellow":
    print("You found 5 cents!!! YOU WIN")
elif doors == "Blue" or doors == "blue":
    print("Game over, because yes")
else:
    print("Game over becaue no")
