from turtle import Turtle

FONT = ("Courier", 24, "normal")
START_POS = (-220, 260)


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.level = 1
        self.update_level()

    def update_level(self):
        self.clear()
        self.goto(START_POS)
        self.write(f"Level {self.level}", align="center", font=FONT)

    def new_level(self):
        self.level += 1
        self.update_level()
