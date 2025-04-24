import random
import time
from turtle import Screen
from game_entities.scoreboard import Scoreboard
from game_entities.player import Player
from game_entities.vehicles import Vehicle


screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)



player = Player()
placar = Scoreboard()

vehicle = Vehicle()


screen.listen()
screen.onkey(player.go_up, "Up")
screen.onkey(player.go_down, "Down")
screen.onkey(player.go_left, "Left")
screen.onkey(player.go_right, "Right")


game_is_on = True

random_num = random.randint(0, 10)



while game_is_on:
    time.sleep(0.1)
    screen.update()

    vehicle.create_car()
    vehicle.move_cars()

    #In case the player wins
    if player.ycor() >= 280:
        placar.increaseScore()
        player.go_to_start()


    #In case the player loses
    for car in vehicle.all_cars:
        if player.distance(car) < 30:
            placar.game_over()
            player.go_to_start()
            game_is_on = False




screen.exitonclick()