import turtle

def draw_square(bred):
    i = 0
    while(i < 4):
        bred.forward(100)
        bred.right(90)
        i = i + 1

def draw_circle(bred):
    bred.circle(100)

def draw_triangle(bred):
    i = 0
    while(i < 3):
        bred.forward(100)
        bred.right(120)
        i = i + 1

window = turtle.Screen()
window.bgcolor("red")

bred = turtle.Turtle()

bred.shape("turtle")
bred.color("yellow")
bred.speed(2)
draw_square(bred)

bred.shape("arrow")
bred.color("blue")
draw_circle(bred)

bred.shape("turtle")
bred.color("green")
draw_triangle(bred)

window.exitonclick()
