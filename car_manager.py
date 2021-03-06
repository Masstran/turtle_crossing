from car import Car
from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
START_CARS = 10
CAR_SPAWN_PAUSE = 10

SPAWN_Y_RANGE_FROM = -250
SPAWN_Y_RANGE_TO = 250
SPAWN_X = 340

END_X = -350


class CarManager:
    def __init__(self):
        self.cars = []
        self.level = 0
        self.speed = STARTING_MOVE_DISTANCE
        self.pause = CAR_SPAWN_PAUSE
        self.create_scene()

    def create_scene(self):
        for _ in range(START_CARS):
            self.create_car()
            for _ in range(CAR_SPAWN_PAUSE - self.level):
                self.move_cars()

    def create_car(self):
        color = random.choice(COLORS)
        random_generate_to = (SPAWN_Y_RANGE_TO - SPAWN_Y_RANGE_FROM) // 20
        y_pos = random.randint(0, random_generate_to) * 20 + SPAWN_Y_RANGE_FROM
        position = (SPAWN_X, y_pos)
        self.cars.append(Car(color, position))

    def move_cars(self):
        for car in self.cars:
            car.move(self.speed)
            if car.xcor() < END_X:
                self.cars.remove(car)
        self.pause -= 1
        if self.pause == 0:
            self.pause = max(CAR_SPAWN_PAUSE - self.level, 1)
            self.create_car()

    def level_up(self):
        self.speed += MOVE_INCREMENT
        self.level += 1

    def is_collision(self, player: Turtle):
        for car in self.cars:
            if abs(car.xcor() - player.xcor()) < 30 and abs(car.ycor() - player.ycor()) < 20:
                return True
        return False
