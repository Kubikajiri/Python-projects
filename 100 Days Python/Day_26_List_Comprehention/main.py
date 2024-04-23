student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    print(key)
    print(value)
    pass

import pandas
student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    print(index)
    print(row.student)
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}
data = pandas.read_csv('nato_phonetic_alphabet.csv')

nato_dict = {codes.letter: codes.code for (letters, codes) in data.iterrows()}
print(nato_dict)
#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
word = input("Type in one word to code\n").upper()
letter_list = []
code_list = []
for letter in word:
    letter_list.append(letter)
    letter_coded = nato_dict[letter]
    code_list.append(letter_coded)
print(code_list)


