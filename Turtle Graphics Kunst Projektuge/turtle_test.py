import turtle  # this imports a library called "turtle". A library is (someone else's) python code, that you can use in your own program.
# The official documentation for turtle is here: https://docs.python.org/3.3/library/turtle.html.

def some_turtle_function(myturtle):
    myturtle.forward(100)

def some_other_turtle_function(myturtle):
    myturtle.right(90)
    myturtle.forward(150)
    myturtle.right(70)
    myturtle.forward(50)

def main():
    myturtle = turtle.Turtle()  # create an object of type Turtle
    some_turtle_function(myturtle)
    some_other_turtle_function(myturtle)
    turtle.done()  # keeps the turtle window open after the program is done

# My stuff here

def visible(turtle_name):
    x = turtle_name.position()[0]
    y = turtle_name.position()[1]
    if x in range(-480, 480) and y in range(-480, 480):
        return 0

def many_squares(turtle, amount, size, distance):
    for _ in range(amount):
        square(turtle, size)
        turtle.penup()
        turtle.forward(distance)
        turtle.pendown()

def square(turtle, length):
    for _ in range(4):
        turtle.forward(length)
        turtle.right(90)

tom = turtle.Turtle()
tom.speed(1)

many_squares(tom,3, 50, 100)
turtle.done()







if __name__ == '__main__':  # is this file run as the main program (as opposed to being imported)?
    main()