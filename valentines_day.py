import turtle

romeo = turtle.Turtle()
romeo.shape("turtle")
romeo.color("IndianRed")


def draw_heart():
    romeo.begin_fill()
    romeo.fillcolor('LightPink2')
    romeo.left(140)
    romeo.forward(180)
    romeo.circle(-90, 200)

    romeo.setheading(60)
    romeo.circle(-90, 200)
    romeo.forward(180)
    romeo.end_fill()


turtle.setup(600, 600)  # Set up the screen size
draw_heart()
romeo.write("Be My Valentine", align= "center", font=("Arial", 25, "bold"))

turtle.done()
