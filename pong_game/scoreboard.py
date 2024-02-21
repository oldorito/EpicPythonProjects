from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-100, 190)
        self.write(self.l_score, align="center", font=("Impact", 70, "normal"))
        self.goto(100, 190)
        self.write(self.r_score, align="center", font=("Impact", 70, "normal"))

    def r_scores(self):
        self.r_score += 1
        self.update_score()

    def l_scores(self):
        self.l_score += 1
        self.update_score()
