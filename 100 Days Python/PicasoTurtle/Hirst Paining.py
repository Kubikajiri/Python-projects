import colorgram
import random
import turtle as t
from turtle import Turtle, Screen
from random import randint
screen = Screen()
timmy = Turtle()
timmy.shape("turtle")
timmy.color("red")
timmy.pencolor("blue")


def random_color():

	t.colormode(255)
	color_pick = random.choice(empty_list)
	return timmy.dot(20,color_pick)


colors = colorgram.extract("image.jpg", 25)
empty_list = []
for color in colors:
	rgb = color.rgb
	red = rgb.r
	green = rgb.g
	blue = rgb.b
	color_tuple = (red, green, blue)
	empty_list.append(color_tuple)

for n in range(0, 400, 40):
	timmy.goto(0, n)
	for _ in range(10):
		random_color()
		timmy.penup()
		timmy.forward(50)



