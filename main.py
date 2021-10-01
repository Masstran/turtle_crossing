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
screen.onkey(key='Up', fun=player.move)

game_is_on = True


while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.move_cars()
    if player.is_win():
        player.reset()
        car_manager.level_up()
        scoreboard.update_score()

    # Collision detection
    if car_manager.is_collision(player):
        game_is_on = False

scoreboard.game_over()
screen.update()
screen.exitonclick()
