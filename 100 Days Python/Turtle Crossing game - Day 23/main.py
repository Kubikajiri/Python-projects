import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move, "w")

game_is_on = True
while game_is_on:
    scoreboard.update_scoreboard()
    time.sleep(0.1)
    screen.update()
    car_manager.create_cars()
    car_manager.move_cars()

    # Detecting collisions
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            print("Game Over!")
    # Detecting reaching the end of the road

    if player.is_at_fline():
        player.start_again()
        car_manager.level_up()
        scoreboard.level_update()



screen.exitonclick()
