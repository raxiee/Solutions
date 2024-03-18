import turtle
from random import random


def draw_barnsley_fern(iterations):
    global x, y  # Declare x and y as global variables

    turtle.speed(0)
    turtle.hideturtle()
    turtle.penup()
    turtle.setpos(0, -300)
    turtle.pendown()

    for _ in range(iterations):
        r = random()
        if r < 0.01:
            xn = 0.0
            yn = 0.16 * y
        elif r < 0.86:
            xn = 0.85 * x + 0.04 * y
            yn = -0.04 * x + 0.85 * y + 1.6
        elif r < 0.93:
            xn = 0.2 * x - 0.26 * y
            yn = 0.23 * x + 0.22 * y + 1.6
        else:
            xn = -0.15 * x + 0.28 * y
            yn = 0.26 * x + 0.24 * y + 0.44

        turtle.penup()
        turtle.setpos(xn * 50, yn * 50)  # Scale up the coordinates for better visibility
        turtle.pendown()
        turtle.dot(2, "green")

        x = xn
        y = yn


# Initial variables
x = 0.0
y = 0.0

# Set the number of iterations
iterations = 10000

# Draw Barnsley Fern fractal
draw_barnsley_fern(iterations)

# Keep the window open
turtle.done()
