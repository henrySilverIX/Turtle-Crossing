from turtle import Turtle
import random


colors = ["red", "blue", "white", "green", "orange"]


class Vehicle(Turtle):
    def __init__(self):
        super().__init__()
        self.random_y = random.randint(-250, 250)
        random_index = random.randint(0, len(colors) - 1)
        self.penup()
        self.goto(370, self.random_y)

        self.color(colors[random_index])
        self.setheading(180)
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=2)


    def move(self, speed):
        new_x = self.xcor() - speed
        self.goto(new_x, self.ycor())

        if self.xcor() < -370:
            self.go_to_start()

    def go_to_start(self):
        self.goto(370, self.random_y)

    def stop(self):
        self.goto(self.xcor(), self.ycor())