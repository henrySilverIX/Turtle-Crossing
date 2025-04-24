from turtle import Turtle

MOVE_DISTANCE = 20



class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.go_to_start()
        self.shape("turtle")
        self.color("white")
        self.setheading(90)


    def go_up(self):
        if self.ycor() < 280:
            new_y = self.ycor() + MOVE_DISTANCE
            self.goto(self.xcor(), new_y)

    def go_down(self):
        if self.ycor() > -280:
            new_y = self.ycor() - MOVE_DISTANCE
            self.goto(self.xcor(), new_y)

    def go_left(self):
        if self.xcor() > -390:
            new_x = self.xcor() - MOVE_DISTANCE
            self.goto(new_x, self.ycor())

    def go_right(self):
        if self.xcor() < 390:
            new_x = self.xcor() + MOVE_DISTANCE
            self.goto(new_x, self.ycor())

    def go_to_start(self):
        self.goto(-270, -280)