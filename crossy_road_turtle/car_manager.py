from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
START_POS_X = 300

HEADING = 180


class CarManager():
    def __init__(self):
        self.cars = []
        self.moving_speed = 0.1

    def create_car(self):
        random_num = random.randint(1, 6)
        if random_num == 1:
            car = Turtle()
            car.shape("square")
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.penup()
            car.color(random.choice(COLORS))
            car.setheading(HEADING)
            start_pos_y = random.randint(-260, 270)
            car.goto(START_POS_X, start_pos_y)
            self.cars.append(car)

    def move_cars(self):
        for car in self.cars:
            car.forward(STARTING_MOVE_DISTANCE)

    def increase_speed(self):
        self.moving_speed *= 0.9
