# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("./Input/Names/invited_names.txt") as names:
	input_letter = names.readlines()
	print(input_letter)

	for name in input_letter:
		with open("./Input/Letters/starting_letter.txt", mode="r") as letter:
			letter_text = letter.read()
			stripped_name = name.strip()
			new_email = letter_text.replace("[name]", stripped_name)
		with open(f"./Output/ReadyToSend/letter_for_{stripped_name}", mode="w") as ready_email:
			ready_email.write(new_email)

