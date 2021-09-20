import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

car_manager = CarManager()

game_is_on = True

count = 0
while game_is_on:
    time.sleep(0.1)
    screen.update()
    if count == 10:
        car_manager.create_car()
        count = 0
    count += 1
    car_manager.move_cars()
