from turtle import Screen
from snake import Snake
import time
from food import Food
from scoreboard import Scoreboard
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

food = Food()
food.reposition()

snake = Snake()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


game_is_on = True
while game_is_on:
	screen.update()
	time.sleep(0.1)
	snake.move()
	if snake.snake_segments[0].distance(food) < 15:
		scoreboard.increase_score()
		food.reposition()
		snake.extend()

	for segment in snake.snake_segments[1:]:
		if snake.snake_segments[0].distance(segment) <= 10:
			game_is_on = False
			scoreboard.reset()

	if snake.snake_segments[0].xcor() >= 290 or snake.snake_segments[0].xcor() <= -290 or snake.snake_segments[0].ycor() >= 290 or snake.snake_segments[0].ycor() <= -290:
		game_is_on = False
		scoreboard.reset()



