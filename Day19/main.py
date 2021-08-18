from turtle import Turtle, Screen

leo = Turtle()
screen = Screen()

def move_forwards():
    leo.forward(10)


screen.listen()
screen.onkey(key="space", fun=move_forwards)
screen.exitonclick()