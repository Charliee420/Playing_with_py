import turtle, math

t = turtle.Turtle()
t.speed(0)
t.color("brown")
turtle.bgcolor("black")
phi = (1 + math.sqrt(5)) / 2

def draw_branch(length):
    if length < 10:
        t.color("red")
        t.begin_fill()
        t.left(140)
        t.forward(10)
        t.circle(-5, 200)
        t.left(120)
        t.circle(-5, 200)
        t.forward(10)
        t.end_fill()
        t.right(140)
        t.color("brown")
        return

    t.forward(length)
    t.right(30)
    draw_branch(length / phi)
    t.left(60)
    draw_branch(length / phi)
    t.right(30)
    t.backward(length)

t.penup()
t.goto(0, -250)
t.pendown()
t.left(90)
draw_branch(100)

t.hideturtle()
turtle.done()
