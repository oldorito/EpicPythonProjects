import random
from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Gambling Zone", prompt="Which turtle will win? Enter a color:\nred, orange, yellow, green, blue or purple ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

pen = Turtle()
pen.penup()
pen.hideturtle()
pen.goto(x=0, y=130)
pen.write("Welcome to Ola's BRUTAL Turtle Race!", align='center', font=('Arial', 18, 'normal'))
pen. goto(x=0, y=110)
pen.write("Which turtle will win?", align='center', font=('Arial', 10, 'normal'))

# timmy = Turtle(shape="turtle")
# timmy.penup()
# timmy.goto(x=-230, y=-100)
racers = []
is_race_on = True
for my_color in colors:
    turtle = Turtle(shape="turtle")
    turtle.color(my_color)
    turtle.penup()
    racers.append(turtle)

y_pos = -120
for racer in racers:
    racer.goto(x=-230, y=y_pos)
    y_pos += 30

if user_bet:
    is_race_on = True

while is_race_on:

    for racer in racers:
        if racer.xcor()>230:
            is_race_on = False
            winner = racer.pencolor()
            if winner == user_bet:
                print(f"You've won! The {winner} turtle is the winner.")
            else:
                print(f"You've lost. The {winner} turtle has won.")

        racing_distance = random.randint(0, 10)
        racer.forward(racing_distance)


screen.exitonclick()