import random
import turtle as t
from turtle import Turtle, Screen
from random import randint
screen = Screen()
timmy = Turtle()
timmy.shape("turtle")
timmy.color("red")
timmy.pencolor("blue")


def pick_random_direction():
	pick = random.randint(1, 5)
	if pick == 1 or pick == 4:
		return timmy.forward(10)
	elif pick == 2:
		return timmy.left(90)
	elif pick == 3:
		return timmy.right(90)


for n in range(100):
	red = (randint(0, 255))
	green = (randint(0, 255))
	blue = (randint(0, 255))
	rgb = (red, green, blue)
	t.colormode(255)
	timmy.pencolor(rgb)
	pick_random_direction()

screen.exitonclick()


