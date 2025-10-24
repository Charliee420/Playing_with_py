import turtle
import math

# Setup
t = turtle.Turtle()
t.speed(0)
t.left(90)  # face upward
t.color("green")
turtle.bgcolor("black")

# Golden ratio
phi = (1 + math.sqrt(5)) / 2  # ≈ 1.618

# Recursive branch drawing
def draw_branch(length):
    if length < 5:  # stop when branches get too small
        return
    t.forward(length)
    
    # turn right for one branch
    t.right(30)
    draw_branch(length / phi)
    
    # turn left twice that angle for the other branch
    t.left(60)
    draw_branch(length / phi)
    
    # restore angle and go back
    t.right(30)
    t.backward(length)

# Start drawing
t.penup()
t.goto(0, -250)
t.pendown()
draw_branch(120)

turtle.done()
