import turtle

def draw_square(bred):
    i = 0
    for i in range(1,5):
        bred.forward(100)
        bred.right(90)

window = turtle.Screen()
window.bgcolor("red")

bred = turtle.Turtle()

bred.shape("turtle")
bred.color("yellow")
bred.speed(5)
for i in range(1,37):
    draw_square(bred)
    bred.right(10)

window.exitonclick()
