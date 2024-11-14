import turtle

screen = turtle.Screen()
screen.bgcolor("white")

pen = turtle.Turtle()
pen.speed(1)

colors = ["purple", "blue", "red", "green", "orange"]
color_index = 0
position = (-200, -50)

def draw_text(x, y):
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    pen.color(colors[color_index])
    pen.write("Head isadepäeva!", font=("Arial", 24, "bold"))

def change_color_and_move(x, y):
    global color_index, position
    color_index = (color_index + 1) % len(colors)
    position = (position[0] + 20, position[1] + 20)
    draw_text(position[0], position[1])

draw_text(position[0], position[1])
screen.onscreenclick(change_color_and_move)

turtle.done()
