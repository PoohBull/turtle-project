import turtle

turtle.shape("turtle")  # optional draws a small turtle as a cursor
turtle.speed(0)  # optional
turtle.pencolor("red")
turtle.pensize(10)


def rec_parameters(length, width):
    for i in range(4):
        turtle.forward(length)
        turtle.right(90)
        turtle.forward(width)
        turtle.right(90)


rec_parameters(100, 50)


def tri_parameters(side):
    for i in range(3):
        turtle.forward(side)
        turtle.left(120)


tri_parameters(100)

turtle.Screen().exitonclick()
#
