from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make yout bet", prompt="Which turtle will win the race? Enter a color: ")
all_turtles = []

colors = ["red", "green", "yellow","orange","purple","blue"]
def generate_turtle(turtle, color, x, y):
    turtle.color(color)
    turtle.penup()
    turtle.goto(x, y)

for i in range(5):
    new_turtle = Turtle(shape="turtle")
    generate_turtle(new_turtle, colors[i], -230, -100+50*i)
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
        random_distance = random.randint(0,10)
        turtle.forward(random_distance)



screen.exitonclick()