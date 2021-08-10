# from turtle import Turtle, Screen
import random
import turtle as t

# leo_the_turtle = t.Turtle()
# leo_the_turtle.shape("turtle")
# leo_the_turtle.color("red")

# Draw Square Box
# for _ in range(4):
#     leo_the_turtle.forward(100)
#     leo_the_turtle.right(90)

# Draw Dash Line
# for _ in range(10):
#     leo_the_turtle.forward(10)
#     leo_the_turtle.penup()
#     leo_the_turtle.forward(10)
#     leo_the_turtle.pendown()


# Draw Shapes
# def draw_shape(num_sides):
#     angle = round(360 / num_sides)
#     for _ in range(num_sides):
#         print(angle)
#         leo_the_turtle.forward(100)
#         leo_the_turtle.right(angle)
# for shape_side_n in range(3,10):
#     draw_shape(shape_side_n)

# colors = ["blue", "red", "yellow", "purple", "gold", "brown", "pink"]
leo = t.Turtle()
# directions = [0, 90, 180, 270]
# leo.pensize(15)
# leo.speed("fast")
# for _ in range(200):
#     leo_the_turtle.forward(50)
#     leo_the_turtle.setheading(random.choice(directions))
#     leo_the_turtle.color(random.choice(colors))


t.colormode(255)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    random_color = (r, g, b)
    return random_color
#
# for _ in range(200):
#     leo.color(random_color())
#     leo.forward(30)
#     leo.setheading(random.choice(directions))
t.speed("fastest")

def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        leo.color(random_color())
        leo.circle(100)
        leo.setheading(leo.heading() + size_of_gap)

draw_spirograph(5)

screen = t.Screen()
screen.onclick(leo.goto)
