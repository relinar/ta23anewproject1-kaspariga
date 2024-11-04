import turtle
import random

t = turtle.Turtle()
i = 1
t.color("blue")
t.left(90)
t.speed(1000)
colors = ["blue", "pink", "violet", "purple", "red"]  # Use a list instead of a set

while i < 150:
    t.color(random.choice(colors))  # Choose a random color here
    t.forward(100)
    t.right(185)
    i += 1

turtle.Screen().exitonclick()
