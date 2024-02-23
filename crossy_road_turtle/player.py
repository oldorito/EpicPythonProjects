from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
HEADING = 90


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("DarkGreen")
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(HEADING)

    def move(self):
        self.forward(MOVE_DISTANCE)

    def reset_pos(self):
        self.goto(STARTING_POSITION)
