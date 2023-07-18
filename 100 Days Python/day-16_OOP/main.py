# import turtle
# from turtle import Turtle, Screen
#
# timmy = Turtle()
# my_screen = Screen()
#
# print(my_screen.canvheight)
# timmy.shape("turtle")
# timmy.color("chartreuse4")
#
# timmy.forward(100)
# my_screen.exitonclick()
#

from prettytable import PrettyTable

table = PrettyTable()

table.add_column("Pokemon", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Element", ["Electric", "Water", "Fire"])
table.align = "l"
print(table)