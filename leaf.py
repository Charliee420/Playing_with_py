import turtle
import math

t = turtle.Turtle()
t.speed(0)
t.color("green")

phi = (1 + math.sqrt(5)) / 2

# Draw spiral using golden ratio growth
a = 2  # base radius
for i in range(80):
    angle = i * 137.5  # golden angle
    r = a * (phi ** (i / 10))  # radius grows by golden ratio
    x = r * math.cos(math.radians(angle))
    y = r * math.sin(math.radians(angle))
    t.goto(x, y)
    t.dot(6, "lime")

turtle.done()
