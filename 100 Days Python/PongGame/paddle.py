from turtle import Turtle

class Paddle(Turtle):
	def __init__(self, position):
		super().__init__()
		self.shape("square")
		self.color("white")
		self.shapesize(stretch_wid=5, stretch_len=1)
		self.penup()
		self.goto(position, 0)


	def go_up(self):
		new_y_up = self.ycor() + 20
		self.goto(self.xcor(), new_y_up)

	def go_down(self):
		new_y_down = self.ycor() - 20
		self.goto(self.xcor(), new_y_down)
