import turtle  # this imports a library called "turtle". A library is (someone else's) python code, that you can use in your own program.
# The official documentation for turtle is here: https://docs.python.org/3.3/library/turtle.html.

# def some_turtle_function(myturtle):
#     myturtle.forward(100)

# def some_other_turtle_function(myturtle):
#     myturtle.right(90)
#     myturtle.forward(150)
#     myturtle.right(70)
#     myturtle.forward(50)

# def main():
#     myturtle = turtle.Turtle()  # create an object of type Turtle
#     some_turtle_function(myturtle)
#     some_other_turtle_function(myturtle)
#     turtle.done()  # keeps the turtle window open after the program is done

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
        print(f'Tom is now at {tom.position()}, x-value: {tom.position()[0]=:.2f}, y-value: {tom.position()[1]=:.2f}')
        print(visible(tom))


def many_squares_spinning(amount, size, distance, spin):
    global tom
    for _ in range(amount):
        square(tom, size)
        tom.penup()
        tom.forward(distance)
        tom.pendown()
        tom.right(spin)
        print(f'Tom is now at {tom.position()}, x-value: {tom.position()[0]=:.2f}, y-value: {tom.position()[1]=:.2f}')
        print(visible(tom))


tom = turtle.Turtle()
tom.speed(0)


def main():
    many_squares_spinning(100, 250, 30, 25)
    turtle.done()


if __name__ == '__main__':  # is this file run as the main program (as opposed to being imported)?
    main()