# # For loop
# fruits = ["Apple", "Peach", "Pear"]
#
# for fruit in fruits:
#     print(fruit)
#     print(fruit + "Pie")

# Password Generator Project

import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
           'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
           'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password_length = nr_letters + nr_symbols + nr_numbers


password_letters = []
for l in range(0, nr_letters):
    random_letter = random.randint(0, len(letters) - 1)
    password_letters.append(letters[random_letter])
print(password_letters)

password_numbers = []
for n in range(0, nr_numbers):
    random_number = random.randint(0, len(numbers) - 1)
    password_numbers.append(numbers[random_number])
print(password_numbers)

password_symbols = []
for s in range(0, nr_symbols):
    random_symbol = random.randint(0, len(symbols) - 1)
    password_symbols.append(symbols[random_symbol])
print(password_symbols)

merged_password = password_letters + password_symbols + password_numbers
print(merged_password)

random.shuffle(merged_password)

print(merged_password)


print(f"Your new password is: {merged_password}")

# Eazy Level - Order not randomised:
# e.g. 4 letter, 2 symbol, 2 number = JduE&!91

# Hard Level - Order of characters randomised:
# e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P