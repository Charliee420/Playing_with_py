import turtle, math

t = turtle.Turtle()
t.speed(0)
turtle.bgcolor("black")
t.color("cyan")

phi = (1 + math.sqrt(5)) / 2
radius = 100

for i in range(30):
    t.penup()
    t.goto(0, 0)
    t.pendown()
    t.circle(radius)
    radius *= 1 / phi
    t.right(360 / phi)

t.hideturtle()
turtle.done()
