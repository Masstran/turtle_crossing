from turtle import Turtle


class Car(Turtle):
    def __init__(self, color, position, speed):
        super().__init__()
        self.color(color)
        self.penup()
        self.shape("square")
        self.goto(position)
        self.move_speed = speed
        self.shapesize(stretch_len=2)
        self.setheading(180)

    def move(self):
        self.forward(self.move_speed)


