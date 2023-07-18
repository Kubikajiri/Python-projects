from turtle import Turtle


class Snake:
	def __init__(self):
		self.snake_segments = []
		self.create_snake()

	def create_snake(self):
		x_coord = 0
		for position in range(3):
			tim = Turtle(shape="square")
			self.snake_segments.append(tim)
			tim.color("white")
			tim.penup()
			tim.goto(x=x_coord, y=0)
			x_coord -= 20

	def add_segment(self, position):
		new_segment = Turtle("square")
		new_segment.color("white")
		new_segment.penup()
		new_segment.goto(position)
		self.snake_segments.append(new_segment)

	def extend(self):
		self.add_segment(self.snake_segments[-1].position())

	def reset(self):
		for segment in self.snake_segments:
			segment.goto(10000, 10000)
		self.snake_segments.clear()
		self.create_snake()

	def move(self):

		for seg in range(len(self.snake_segments) - 1, 0, -1):
			new_x = self.snake_segments[seg - 1].xcor()
			new_y = self.snake_segments[seg - 1].ycor()
			self.snake_segments[seg].goto(new_x, new_y)
		self.snake_segments[0].forward(20)

	def up(self):
		if self.snake_segments[0].heading() != 270:
			self.snake_segments[0].setheading(90)

	def down(self):
		if self.snake_segments[0].heading() != 90:
			self.snake_segments[0].setheading(270)

	def left(self):
		if self.snake_segments[0].heading() != 0:
			self.snake_segments[0].setheading(180)

	def right(self):
		if self.snake_segments[0].heading() != 180:
			self.snake_segments[0].setheading(0)