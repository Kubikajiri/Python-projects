from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
turtle = Turtle()
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

l_paddle = Paddle(-350)
r_paddle = Paddle(350)
ball = Ball()
screen.setup(width=800, height=600)
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up, "w")
screen.onkey(r_paddle.go_down, "s")
screen.onkey(l_paddle.go_up, "Up")
screen.onkey(l_paddle.go_down, "Down")


def pong_game():
	game_is_on = True
	while game_is_on:

		screen.update()
		ball.move()
		# Detect the collision
		if ball.ycor() > 280 or ball.ycor() < - 280:
			ball.bounce()
		if ball.distance(r_paddle) < 40 and ball.xcor() > r_paddle.xcor() - 15 or ball.distance(
				l_paddle) < 40 and ball.xcor() < l_paddle.xcor() + 15:
			ball.paddle_bounce()

		elif ball.xcor() >= r_paddle.xcor() + 15 and ball.distance(r_paddle) > 50:
			ball.reset_position()
			scoreboard.l_board()
			if scoreboard.l_score == 3:
				answer = input("Left Pad won! Play again? y/n".lower())
				if answer == "y":
					pong_game()
				else:
					break
			else:
				pong_game()

		elif ball.xcor() <= l_paddle.xcor() + 15 and ball.distance(l_paddle) > 50:
			ball.reset_position()
			scoreboard.r_board()
			if scoreboard.r_score == 3:
				answer = input("Right Pad won! Play again? y/n\n".lower())
				if answer == "y":
					pong_game()
				else:
					break
			else:
				pong_game()
			game_is_on = False


pong_game()
screen.exitonclick()
