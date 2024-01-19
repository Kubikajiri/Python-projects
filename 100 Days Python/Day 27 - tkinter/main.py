from tkinter import *


def calculate():
    miles = int(input.get())
    kilometer = miles * 1.609
    result.config(text=kilometer)


window = Tk()
window.title("Miles to kilometer calc")
window.minsize(width=300, height=200)

# Label
my_label = Label(text="blabla", font=("Comic Sans", 24, "bold"))
my_label.config(text="is equal to")
my_label.grid(column=0, row=1)

kilometer_label = Label(text="kilometer", font=("Comic Sans", 24, "bold"))
kilometer_label.config(text="kilometers")
kilometer_label.grid(column=2, row=1)

miles_label = Label(text="mile", font=("Comic Sans", 24, "bold"))
miles_label.config(text="miles")
miles_label.grid(column=2, row=0)

result = Label(text="", font=("Comic Sans", 24, "bold"))
result.grid(column=1, row=1)
# Button
button = Button(text="calculate", command=calculate)
button.grid(column=1, row=2)

# Entry

input = Entry(width=10)
print(input.get())
input.grid(column=1, row=0)

window.mainloop()