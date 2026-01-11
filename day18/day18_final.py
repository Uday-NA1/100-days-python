import turtle as t
import random

tim = t.Turtle()
t.colormode(255)
tim.speed("fastest")
tim.color("black")

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

def draw_grid(col_size, row_size, dot_size, gap_size):
    tim.hideturtle()
    tim.penup()
    tim.setheading(225)
    tim.forward(250)
    tim.setheading(0)

    for _ in range(col_size):

        for j in range(row_size):
            tim.dot(dot_size, random_color())
            tim.penup()
            tim.forward(gap_size)
            tim.pendown()

        tim.setheading(90)
        tim.penup()
        tim.forward(gap_size)
        tim.setheading(180)
        tim.forward(gap_size * row_size)
        tim.setheading(0)
        tim.pendown()

draw_grid(10, 10, 20, 50)

screen = t.Screen()
screen.exitonclick()