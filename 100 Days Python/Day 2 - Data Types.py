# Working with Data Types
# ------------------------------------------------

# String

print("Hello"[4]) # string indexing - it starts with 0!
# ------------------------------------------------

#Integer

print(123+345)

#Float

3.14159


#Boolean

True

False

# ------------------------------------------------
# Type conversion

num_char = len(input("what's your name?\n"))

num_char_str = str(num_char) # str() takes an object and converts it into a string
num_char_float = float(num_char)
print("your name has", num_char_str, "characters")

# ------------------------------------------------

print(3 * 3 + 3 / 3 - 3)

# Cool operations
print (3**2) # power
print(8//3) # since normal division returns a float, "//" chops off all the decimal numbers, but doesnt round it
# to round the number, use round()
# --------------------------------------------------

# F strings

# Old model
score = 90
height = 1.2
isWinning = True
print("your score is", score)  # produces error and will take a lot of time to make it work

# f_String

print(f"your score is {score}, your height is {height}, and youre winning is{isWinning}")

# -------------------------------------------------------
# Project!
# If the bill was $150.00, split between 5 people, with 12% tip.

# Each person should pay (150.00 / 5) * 1.12 = 33.6

# Format the result to 2 decimal places = 33.60

# Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

# Write your code below this line 👇

bill = float(input("What was the total bill?\n"))
tip_precetnage = (int(input("What percentage of tip would you like to get? 10, 12, 15?\n"))+100)/100
guest_value = int(input("How many people were at the table?\n"))

payment = round((bill*tip_precetnage)/guest_value, 2)

print(f"Each person should pay {payment}$")