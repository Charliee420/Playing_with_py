import turtle, math

t = turtle.Turtle()
t.speed(0)
t.color("orange")
turtle.bgcolor("black")

fib = [1, 1]
for _ in range(10):
    fib.append(fib[-1] + fib[-2])

for i in range(len(fib)):
    t.circle(fib[i] * 10, 90)
    t.forward(fib[i] * 10)

t.hideturtle()
turtle.done()
