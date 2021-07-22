import turtle
import random
import time

wn = turtle.Screen()
wn.title("Tic Tac Toe")
wn.setup(width=600, height=600)
wn.bgcolor("Black")
wn.tracer(0)
wn.listen()

grid = turtle.Turtle()
grid.color("White")
grid.speed(0)
grid.pensize(width=5)
grid.penup()
grid.goto(-300, 300)
grid.pendown()
for i in range(4):
    grid.forward(600)
    grid.right(90)
    for j in range(4):
        grid.forward(200)
        grid.right(90)
grid.penup()
grid.goto(-100, 100)
grid.pendown()
for k in range(4):
    grid.forward(200)
    grid.right(90)
grid.penup()


xclick = 0
yclick = 0

x = grid.xcor()
y = grid.ycor()

def cross(x,y):
    grid.goto(x, y)
    grid.pendown()
    grid.goto(x+200, y+200)
    grid.goto(x, y+200)
    grid.goto(x+200,y)
    grid.penup()

def getcoordinates():
    turtle.onscreenclick(modifyglobalvariables)


def modifyglobalvariables(rawx, rawy):
    global xclick
    global yclick
    xclick = int(rawx // 1)
    yclick = int(rawy // 1)

    def move(xclick, yclick):
        if -300 < xclick < -100 and 100 < yclick < 300:
            cross(-300,100)
        if -300 < xclick < -100 and -100 < yclick < 100:
            cross(-300, -100)
        if -300 < xclick < -100 and -300 < yclick < -100:
            cross(-300, -300)
        if -100 < xclick < 100 and 100 < yclick < 300:
            cross(-100, 100)
        if -100 < xclick < 100 and -100 < yclick < 100:
            cross(-100, -100)
        if -100 < xclick < 100 and -300 < yclick < -100:
            cross(-100, -300)
        if 100 < xclick < 300 and 100 < yclick < 300:
            cross(100,100)
        if 100 < xclick < 300 and -100 < yclick < 100:
            cross(100, -100)
        if 100 < xclick < 300 and -300 < yclick < -100:
            cross(100, -300)
    return move(xclick,yclick)

getcoordinates()


while True:
    wn.update()
