from turtle import Turtle


class Car(Turtle):
    def __init__(self, color, position):
        super().__init__()
        self.color(color)
        self.penup()
        self.shape("square")
        self.goto(position)
        self.shapesize(stretch_len=2)
        self.setheading(180)

    def move(self, speed):
        self.forward(speed)


