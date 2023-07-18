import random

# c = random.randint(100, 200)
# print(c)

# Python List - IMPORTANT
# The order is SUUUUUPER IMPORTANT -
# states_of_america = ["Delaware", "Pennsylvania"]
#
# states_of_america.append("Jerzyland")
#
# states_of_america.extend(["Angelaland", "Tomorrowland", 5, True])
#
# # The dirty dozen list
#
# dirty_dozen = ["Strawberries", "Spinach", "Kale", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears", "Tomatoes", "Celery", "Potatoes"]
#
# fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
# veggies = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
#
# dirty_dozen = [fruits, veggies]
#
# r1 = [2, 4, 5]
# map = [r1]
#
#

# print(map[0][2])


rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Write your code below this line 👇

choice = int(input("Welcome to the greatest battle of the century! Choose: 0 - rock, 1 - paper or 2 - scissors?"))
print(choice)
computer_hand = [rock, paper, scissors]
computer_choice = random.randint(0, 2)
if computer_hand[choice] == rock and computer_hand[computer_choice] == rock:
    print(computer_hand[computer_choice])
    print("It's a draw! You made a small fistbump with eachother")
elif computer_hand[choice] == rock and computer_hand[computer_choice] == paper:
    print(computer_hand[computer_choice])
    print("Ahh, you got wrapped around like a nice burrito. You lost :(")
elif computer_hand[choice] == rock and computer_hand[computer_choice] == scissors:
    print(computer_hand[computer_choice])
    print("Congratulations you've won!. The scissors aren't a threat to Dwayne.")
elif computer_hand[choice] == paper and computer_hand[computer_choice] == rock:
    print(computer_hand[computer_choice])
    print("You wrapped the computer around like an anaconda! You won!")
elif computer_hand[choice] == paper and computer_hand[computer_choice] == paper:
    print(computer_hand[computer_choice])
    print("It's a draw! You gave each other a high five")
elif computer_hand[choice] == paper and computer_hand[computer_choice] == scissors:
    print(computer_hand[computer_choice])
    print("Your paper got shredded to pieces")
elif computer_hand[choice] == scissors and computer_hand[computer_choice] == rock:
    print(computer_hand[computer_choice])
    print("Dang it. The scisors break on stone. Who would've thought")
elif computer_hand[choice] == scissors and computer_hand[computer_choice] == paper:
    print(computer_hand[computer_choice])
    print("Snip snip! You won!")
elif computer_hand[choice] == scissors and computer_hand[computer_choice] == scissors:
    print(computer_hand[computer_choice])
    print("It's a draw")
