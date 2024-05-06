BACKGROUND_COLOR = "#B1DDC6"
from tkinter import *
import pandas as pd
import random
window = Tk()
french_data = pd.read_csv('data\\words_to_learn.csv')
french_data_new = french_data.copy()
random_word = random.randint(0, len(french_data['French']))

try:
	data = pd.read_csv("data\\words_to_learn.csv")
except FileNotFoundError:
	original_data = pd.read_csv("data\\french_words.csv")


def generate_random_french():
	global random_word, flip_timer
	window.after_cancel(flip_timer)
	random_word = random.randint(0, len(french_data['French']))
	canvas.itemconfig(card_title, text="French", fill="black")
	canvas.itemconfig(card_word, text=french_data["French"][random_word], font=("Arial", 30, "bold"), fill="black")
	canvas.itemconfig(card_bg, image=card_front_img)
	flip_timer = window.after(3000, func=flip_card)




def flip_card():
	canvas.itemconfig(card_title, text="English", fill="white")
	canvas.itemconfig(card_word, text=french_data["English"][random_word], fill="white")
	canvas.itemconfig(card_bg, image=card_back_img)


list_of_known_words = []
def is_known():
	global random_word, french_data
	french_data = french_data.drop(random_word)
	data = pd.DataFrame(french_data)
	data.to_csv("data\\words_to_learn.csv")
	generate_random_french()



window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)
canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file="images\\card_front.png")
card_back_img = PhotoImage(file="images\\card_back.png")
card_bg = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 150, font=("Arial", 40, "italic"))
card_word = canvas.create_text(400, 300, font=("Arial", 30, "bold"))

canvas.grid(row=0, column=0, columnspan=2)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)

cross_image = PhotoImage(file='images\\wrong.png')
unknown_button = Button(image=cross_image, highlightthickness=0, command=generate_random_french)
unknown_button.grid(row=1, column=0)

check_image = PhotoImage(file='images\\right.png')
known_button = Button(image=check_image, highlightthickness=0, command=is_known)
known_button.grid(row=1, column=1)


window.mainloop()