import turtle, math

t = turtle.Turtle()
t.speed(0)
turtle.bgcolor("black")
t.color("gold")

phi = (1 + math.sqrt(5)) / 2
golden_angle = 360 / (phi ** 2)

for i in range(600):
    angle = i * golden_angle
    radius = math.sqrt(i) * 8
    x = radius * math.cos(math.radians(angle))
    y = radius * math.sin(math.radians(angle))
    t.goto(x, y)
    t.dot(6, "yellow")

t.hideturtle()
turtle.done()
