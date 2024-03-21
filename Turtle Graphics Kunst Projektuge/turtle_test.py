import turtle  # this imports a library called "turtle". A library is (someone else's) python code, that you can use in your own program.

turtle.setup(width=1400, height=900)

# My stuff here
def visible(turtle_name):
    x = int(turtle_name.position()[0])
    y = int(turtle_name.position()[1])
    if x in range(-480, 480) and y in range(-480, 480):
        return True
    else:
        return False

def square(turtle_name, length):
    for _ in range(4):
        turtle_name.forward(length)
        turtle_name.right(90)


def many_squares(amount, size, distance):
    global tom
    for _ in range(amount):
        square(tom, size)
        tom.penup()
        tom.forward(distance)
        tom.pendown()

def many_squares_spinning(amount, size, distance, spin):
    for _ in range(amount):
        print(f'Tom is now at {tom.position()}, x-value: {tom.position()[0]=:.2f}, y-value: {tom.position()[1]=:.2f}')
        purple_blue(tom)
        square(tom, size)
        tom.penup()
        tom.forward(distance)
        tom.pendown()
        tom.right(spin)

def circle(turtle_name, size):
    for _ in range(72):
        turtle_name.forward(size)
        turtle_name.right(5)


def many_circles(amount, size, distance):
    global tom
    for _ in range(amount):
        circle(tom, size)
        tom.penup()
        tom.left(0)
        tom.forward(distance)
        tom.pendown()

def many_circles_spinning(amount, size, distance, spin):
    global tom
    for i in range(amount):
        if (i % 2) == 0:
            tom.pencolor(0, 0, 255)
            circle(tom, size)
            tom.penup()
            tom.left(0)
            tom.forward(distance)
            tom.pendown()
            tom.right(spin)
        else:
            tom.pencolor(160, 32, 240)
            circle(tom, size)
            tom.penup()
            tom.left(0)
            tom.forward(distance)
            tom.pendown()
            tom.right(spin)

def half_circle(turtle_name, size):
    for _ in range(36):
        turtle_name.forward(size)
        turtle_name.right(5)

def half_circle_2(turtle_name, size):
    for _ in range(33):
        turtle_name.forward(size)
        turtle_name.right(5)

def e_circle(turtle_name, size):
    turtle_name.left(90)
    for _ in range(66):
        turtle_name.forward(size)
        turtle_name.left(5)

def e_circle_2(turtle_name, size):
    turtle_name.left(90)
    for _ in range(32):
        turtle_name.forward(size)
        turtle_name.right(5)

def l_circle(turtle_name, size):
    turtle_name.left(90)
    for _ in range(37):
        turtle_name.forward(size)
        turtle_name.right(5)

def l_circle_2(turtle_name, size):
    for _ in range(37):
        turtle_name.forward(size)
        turtle_name.right(5)


def break_coordinates(turtle_name, x_break, y_break):# Useless, just use turtle.goto instead
    x = int(turtle_name.position()[0])
    y = int(turtle_name.position()[1])
    if x == x_break and y == y_break:
        turtle_name.forward(0)
    else:
        turtle_name.forward(1)

def letter_P(start_x, start_y):
    global tom
    tom.penup()
    tom.goto(start_x, start_y)
    tom.pendown()
    tom.left(90)
    tom.forward(170)
    tom.right(90)
    tom.forward(20)
    half_circle(tom,4)
    tom.left(90)
    tom.goto(start_x + 24, start_y)
    tom.goto(start_x, start_y)
    tom.penup()
    tom.goto(start_x + 24, start_y + 150)
    tom.left(87)
    tom.pendown()
    half_circle(tom,2)
    tom.goto(start_x + 24, start_y + 150)
    tom.penup()
    tom.home()

def letter_e(start_x, start_y):
    global tom
    tom.penup()
    tom.goto(start_x, start_y)
    tom.pendown()
    e_circle(tom, 4)
    tom.left(90)
    tom.forward(20)
    e_circle_2(tom, 2)
    tom.goto(start_x, start_y)
    tom.penup()
    tom.goto(start_x - 67.52, start_y + 15)
    tom.pendown()
    half_circle_2(tom,2)
    tom.goto(start_x - 67.52, start_y + 15)
    tom.penup()
    tom.home()

def letter_l(start_x, start_y):
    global tom
    tom.hideturtle()
    tom.penup()
    tom.goto(start_x, start_y)
    tom.pendown()
    l_circle(tom,1.5)
    tom.goto(start_x + 34.36, start_y - 150)
    l_circle_2(tom, 1.5)
    tom.goto(start_x,start_y)
    tom.penup()
    tom.home()

def signature():
    tom.pendown()
    letter_P(200 * 1.45, -420)
    letter_e(350 * 1.25, -380)
    letter_l(370 * 1.25, -255)
    letter_l(420 * 1.25, -255)
    letter_e(565 * 1.19, -380)

def purple_blue(turtle_name):
    y = int(turtle_name.ycor())#hej
    turtle.colormode(255)
    if y in range(-100, 14):
        turtle_name.pencolor(0, 0, 255)
    elif y in range(15, 80):
        turtle_name.pencolor(160, 32, 240)
    else:
        turtle_name.pencolor(130, 170, 255)


tom = turtle.Turtle()
tom.speed(0)

def main():
    global tom
    tom.penup()
    tom.goto(-370, 100)
    many_squares_spinning(100, 187.5 * 1.4, 22.5 * 1.4, 25)
    tom.penup()
    tom.home()
    tom.goto(350, 260)
    tom.pendown()
    many_circles_spinning(15, 7.5 * 1.4, 75 * 1.4, 25)
    tom.pencolor(0, 0, 0)
    tom.penup()
    tom.home()
    signature()
    turtle.done()


# many_squares_spinning(100, 250, 30, 25) Original spinning squares
# many_circles_spinning(15, 10, 100, 25) Original spinning circles
if __name__ == '__main__':  # is this file run as the main program (as opposed to being imported)?
    main()