from car import Car
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
SPAWN_Y_RANGE_FROM = -250
SPAWN_Y_RANGE_TO = 270
SPAWN_X = 340


class CarManager:
    def __init__(self):
        self.cars = []
        self.speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        color = random.choice(COLORS)
        random_generate_to = (SPAWN_Y_RANGE_TO - SPAWN_Y_RANGE_FROM) // 20
        y_pos = random.randint(0, random_generate_to) * 20 + SPAWN_Y_RANGE_FROM
        position = (SPAWN_X, y_pos)
        self.cars.append(Car(color, position, self.speed))

    def move_cars(self):
        for car in self.cars:
            car.move()
            if car.xcor() < -350:
                self.cars.remove(car)
