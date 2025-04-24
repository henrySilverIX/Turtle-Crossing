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


vehicles = []
player = Player()
placar = Scoreboard()
for _ in range(10):
    vehicle = Vehicle()
    vehicles.append(vehicle)

screen.listen()
screen.onkey(player.go_up, "Up")
screen.onkey(player.go_down, "Down")
screen.onkey(player.go_left, "Left")
screen.onkey(player.go_right, "Right")


game_is_on = True

random_num = random.randint(0, 4)
print(random_num)


while game_is_on:
    time.sleep(0.1)
    screen.update()

    for i in range(len(vehicles)):
        random_speed = random.randint(1, 20)
        vehicles[i].move(random_speed)

    #In case the player wins
    if player.ycor() >= 280:
        placar.increaseScore()
        player.go_to_start()
        for i in range(len(vehicles)):
            vehicles[i].go_to_start()

    #In case the player loses
    for i in range(len(vehicles)):
        if player.distance(vehicles[i]) < 40:
            placar.game_over()
            player.go_to_start()
            for j in range(len(vehicles)):
                vehicles[j].go_to_start()
                vehicles[j].stop()



screen.exitonclick()