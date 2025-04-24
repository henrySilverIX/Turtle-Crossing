from turtle import Turtle
import random



MOVE_DISTANCE = 10
colors = ["red", "blue", "white", "green", "orange"]


class Vehicle(Turtle):
    def __init__(self):
        super().__init__()
        self.all_cars = []
        self.car_speed = MOVE_DISTANCE


    def create_car(self):
        creating_chance = random.randint(1, 6)

        if creating_chance == 1:
            new_car = Turtle()
            random_y = random.randint(-250, 250)
            new_car.penup()
            new_car.goto(370, random_y)
            new_car.color(random.choice(colors))
            new_car.shape("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            self.all_cars.append(new_car)


    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.car_speed)


    def increase_movement(self):
        self.car_speed += 1

