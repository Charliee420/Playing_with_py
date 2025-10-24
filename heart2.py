import turtle
import math

phi = (1 + math.sqrt(5)) / 2  # golden ratio
t = turtle.Turtle()
t.color("red", "pink")
turtle.bgcolor("black")
t.speed(5)

# Set heart proportions
width = 200
height = width / phi  # height based on golden ratio

t.begin_fill()
t.left(140)
t.forward(height)
t.circle(-width / 4, 200)
t.left(120)
t.circle(-width / 4, 200)
t.forward(height)
t.end_fill()

t.hideturtle()
turtle.done()
