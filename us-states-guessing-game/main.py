import turtle
from turtle import Screen
import pandas

ALIGN = "center"
FONT = ("Arial", 10, "normal")

screen = Screen()
screen.title("Can you name all States of the U.S.?")
background = "blank_states_img.gif"
screen.addshape(background)
turtle.shape(background)

data = pandas.read_csv("50_states.csv")
state_name_list = str(data["state"].to_list)
data_dict = data.to_dict()
guessed_states = []
score = 0


def write_on_map(state, x_pos, y_pos):
    state_title = turtle.Turtle()
    state_title.clear()
    state_title.penup()
    state_title.hideturtle()
    state_title.goto(x_pos, y_pos)
    state_title.write(f"{state}", align=ALIGN, font=FONT)


game_on = True
while game_on:
    state_guess = screen.textinput(title=f"{score}/50 States Guessed", prompt="Name another state").title()
    if state_guess in state_name_list and state_guess not in guessed_states:
        guessed_states.append(state_guess)
        state_data = data[data.state == state_guess]
        x_pos = int(state_data.x)
        y_pos = int(state_data.y)
        write_on_map(state_guess, x_pos, y_pos)
        score += 1

screen.exitonclick()
