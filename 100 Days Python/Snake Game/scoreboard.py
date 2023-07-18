from turtle import Turtle


class Scoreboard(Turtle):
	def __init__(self):
		super().__init__()
		self.score = 0
		with open("data.txt", mode="r+") as score_data:
			self.highscore = int(score_data.read())
		self.goto(x=0, y=280)
		self.color("white")
		self.hideturtle()
		self.update_score()

	def update_score(self):
		self.clear()
		self.write(f"Score: {self.score} High Score = {self.highscore}", False, align="center", font=("Arial", 12, "normal"))

	# def game_over(self):
	# 	self.penup()
	# 	self.goto(0, 0)
	# 	self.write("Game Over", False, align="center", font=("Arial", 14, "bold"))

	def increase_score(self):
		self.score += 1
		self.update_score()

	def reset(self):
		if self.score > int(self.highscore):
			with open("data.txt", mode="w") as highscore_write:
				self.score = highscore_write.write(f"{self.score}")
		self.score = 0
		self.update_score()