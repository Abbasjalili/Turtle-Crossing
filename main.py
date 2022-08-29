from turtle import Screen
from scoreboard import Scoreboard
from cars import Cars
from player import Player
import random
import time


screen = Screen()
screen.setup(width = 600, height= 600)
screen.bgcolor("white")
screen.title("Turtle Crossing")
screen.tracer(0)


level = Scoreboard()
cars = Cars()
player = Player((0, -280))

screen.listen()
screen.onkey(player.up, "Up")


game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(player.move_speed)
    
    cars.create_car()
    cars.move()
    
    for car in cars.cars:
        if car.distance(player) < 20:
            game_is_on = False
            level.game_over()
    else:
        if player.ycor() > 280:
                level.increase_score()

                player.refresh()




screen.exitonclick()