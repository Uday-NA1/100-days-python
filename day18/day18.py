import turtle as t
import random

# import random
# from random import randint
# from random import *
# import turtle as t

tim = t.Turtle()
t.colormode(255)
tim.shape("turtle")
tim.color("red")
tim.speed("fastest")

directions = [0, 90, 180, 270]
colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)

def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        tim.forward(100)
        tim.right(angle)

# POLYGONS
for i in range(3,11):
    tim.color(random.choice(colors))
    draw_shape(i)

# SQUARE
for i in range(4):
    tim.forward(100)
    tim.right(90)

# DOTTED LINE
for i in range(15):
    tim.pendown()
    tim.forward(10)
    tim.penup()
    tim.forward(10)

# RANDOM WALK
tim.pensize(15)
for _ in range(200):
    tim.color(random_color())
    tim.forward(30)
    tim.setheading(random.choice(directions))

# SPIROGRAPH
draw_spirograph(5)

screen = t.Screen()
screen.exitonclick()