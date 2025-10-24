import turtle
import math
import colorsys

turtle.bgcolor("black")
t = turtle.Turtle()
t.speed(0)
t.hideturtle()
t.width(2)

# Stop screen from updating each step
turtle.tracer(0, 0)  

# Color function
def get_color(i, total):
    hue = i / total
    r, g, b = colorsys.hsv_to_rgb(hue, 1, 1)
    return (r, g, b)

phi = (1 + math.sqrt(5)) / 2
total_points = 2000  # more points, faster drawing

for i in range(total_points):
    color = get_color(i, total_points)
    t.pencolor(color)
    angle = i * (360 / (phi ** 2))  # golden angle
    radius = math.sqrt(i) * 4
    x = radius * math.cos(math.radians(angle))
    y = radius * math.sin(math.radians(angle))
    t.goto(x, y)

    if i % 50 == 0:  # update every 50 points
        turtle.update()

turtle.update()
turtle.done()
