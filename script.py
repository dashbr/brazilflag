import turtle


def draw_square(some_turtle, size):
    for num in range(0, 4):
        some_turtle.forward(size)
        some_turtle.right(90)


def draw_circle(some_turtle, radius):
    some_turtle.circle(radius)

window = turtle.Screen()


# draws the Brazillian flag
def draw_art():
    brad = turtle.Turtle()
    brad.shape("classic")
    brad.speed(0)
    brad.color("blue")

    brad.penup()
    brad.goto(-320,200)
    brad.pendown()

    brad.color("#009B3A", "#009B3A")

    brad.begin_fill()
    brad.forward(700)
    brad.right(90)
    brad.forward(400)
    brad.right(90)
    brad.forward(700)
    brad.right(90)
    brad.forward(400)
    brad.right(90)
    brad.end_fill()

    brad.goto(0, 0)

    brad.color("#FEDF00", "#FEDF00")
    brad.begin_fill()
    brad.forward(300)

    brad.color("#FEDF00")
    brad.left(150)
    brad.forward(350)
    brad.left(60)
    brad.forward(350)
    brad.left(120)
    brad.forward(350)
    brad.left(60)
    brad.forward(350)
    brad.end_fill()
    brad.penup()

    brad.right(10)
    brad.back(320)
    brad.setheading(0)

    brad.pendown()

    brad.color("#002776", "#002776")
    brad.begin_fill()

    draw_circle(brad, 110)

    brad.end_fill()

draw_art()

window.exitonclick()
