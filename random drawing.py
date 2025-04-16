import random
import turtle
def draw():
    global drawing
    global commands
    while drawing:
        turtle.speed(5)
        eval(random.choice(commands))
def pause():
    global drawing
    drawing = False
def resume():
    global drawing
    drawing = True
    draw()
def reset():
    global drawing
    drawing = True
    turtle.clear()
    turtle.penup()
    turtle.home()
    turtle.pendown()
    draw()
drawing = True
screen = turtle.Screen()
screen.listen()
screen.onkey(pause, "space")
screen.onkey(reset, "r")
screen.onkey(resume, "c")
turtle.title('random drawing')
random.seed(random.randint(-1000000, 1000000))
commands = ["turtle.forward(random.randint(1, 200))", "turtle.backward(random.randint(1, 200))", "turtle.right(random.randint(1, 359))", "turtle.left(random.randint(1, 359))", "turtle.color(random.random(), random.random(), random.random())", "turtle.width(random.randint(1, 10))"]
draw()
turtle.mainloop()
