from turtle import Turtle
from random import *


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.color("firebrick1")
        self.speed("fastest")
        self.shapesize(stretch_wid=0.7, stretch_len=0.7)
        self.refresh()

    def refresh(self):
        random_x = randint(-280, 280)
        random_y = randint(-280, 280)
        self.goto(random_x, random_y)
