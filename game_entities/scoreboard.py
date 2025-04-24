from turtle import Turtle

ALIGNMENT = "center"
CLASS_FAMILY = "Montserrat"
FONT_SIZE = 8


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(0,280)
        self.score = 0
        self.speed("fastest")
        self.write(f"Score: {self.score}", False, align=ALIGNMENT, font=(CLASS_FAMILY, FONT_SIZE,"normal"))

    def increaseScore(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", False, align=ALIGNMENT, font=(CLASS_FAMILY, FONT_SIZE,"normal"))


    def game_over(self):
        self.clear()
        self.goto(0,0)
        self.write(f"GAME OVER\nScore: {self.score}", False, align=ALIGNMENT, font=(CLASS_FAMILY, FONT_SIZE,"normal"))
