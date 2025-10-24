import turtle
import math
import colorsys

# Setup
turtle.bgcolor("black")
t = turtle.Turtle()
t.speed(0)
t.hideturtle()
t.width(2)
turtle.tracer(0, 0)  # disable automatic updates

# Color function (rainbow)
def get_color(i, total):
    hue = (i / total) % 1.0
    r, g, b = colorsys.hsv_to_rgb(hue, 1, 1)
    return (r, g, b)

phi = (1 + math.sqrt(5)) / 2
i = 0
total_points = 2000

# Infinite animation loop
while True:
    t.clear()  # clear previous frame
    for j in range(total_points):
        angle = (j + i) * (360 / (phi ** 2))  # golden angle offset by i
        radius = math.sqrt(j) * 4
        x = radius * math.cos(math.radians(angle))
        y = radius * math.sin(math.radians(angle))
        t.goto(x, y)
        color = get_color(j + i, total_points)
        t.pencolor(color)
        t.dot(3)
    
    turtle.update()  # update screen after drawing
    i += 5  # shift for rotation effect
