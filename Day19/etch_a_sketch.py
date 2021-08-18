from turtle import Turtle, Screen

leo = Turtle()
screen = Screen()


def move_forwards():
    leo.forward(10)


def move_back():
    leo.back(10)


def turn_right():
    new_heading = leo.left(10) - 10
    leo.setheading(new_heading)


def turn_left():
    new_heading = leo.left(10) + 10
    leo.setheading(new_heading)


def clear():
    leo.clear()
    leo.penup()
    leo.home()
    leo.pendown()

screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_back)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="c", fun=clear)

screen.exitonclick()
