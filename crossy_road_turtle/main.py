import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("grey60")
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_man = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(player.move, "Up")

game_is_on = True
while game_is_on:

    time.sleep(car_man.moving_speed)
    screen.update()

    car_man.create_car()
    car_man.move_cars()

    if player.ycor() > 290:
        scoreboard.new_level()
        car_man.increase_speed()
        player.reset_pos()

    for car in car_man.cars:
        if player.distance(car) < 20:
            game_is_on = False

screen.exitonclick()
