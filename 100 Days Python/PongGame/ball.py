from turtle import Turtle


class Ball(Turtle):
	def __init__(self):
		super().__init__()
		self.shape("circle")
		self.shapesize(1)
		self.goto(0, 0)
		self.color("white")
		self.goto(0, 0)
		self.penup()
		self.x_move = 0.1
		self.y_move = 0.1

	def move(self):
		new_x = self.xcor() + self.x_move
		new_y = self.ycor() + self.y_move
		self.goto(new_x, new_y)

	def bounce(self):
		self.y_move *= -1

	def paddle_bounce(self):
		self.x_move *= -1

	def reset_position(self):
		self.goto(0, 0)
