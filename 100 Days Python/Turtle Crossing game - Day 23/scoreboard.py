FONT = ("Courier", 24, "normal")
from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.level = 1
        self.penup()
        self.goto(-250, 250)

    def update_scoreboard(self):
        self.clear()
        self.write(f'Level: {self.level}', align='left', font=FONT)

    def level_update(self):
        self.level += 1
