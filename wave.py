import turtle, math

t = turtle.Turtle()
t.speed(0)
t.color("magenta")
turtle.bgcolor("black")

phi = (1 + math.sqrt(5)) / 2

for x in range(-360, 360):
    y = 100 * math.sin(math.radians(x)) + (x / phi)
    t.goto(x, y)

t.hideturtle()
turtle.done()
