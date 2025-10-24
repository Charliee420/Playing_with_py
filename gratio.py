import turtle
import math

# Setup screen and turtle
t = turtle.Turtle()
t.speed(0)
turtle.bgcolor("black")
t.color("lime")

# Golden ratio and golden angle
phi = (1 + math.sqrt(5)) / 2
golden_angle = 360 / (phi ** 2)  # ≈ 137.5°

# Draw pattern
for i in range(200):
    t.forward(math.sqrt(i) * 10)
    t.dot(10, "green")
    t.backward(math.sqrt(i) * 10)
    t.right(golden_angle)

turtle.done()
