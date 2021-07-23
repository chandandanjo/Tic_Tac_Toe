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

shape = wn.numinput("Cross or Circle ?", "For cross enter: 1, For circle enter: 0", minval=0, maxval=1)

p_cross = 0
p_circle = 0

c1 = 0
c2 = 0
c3 = 0
c4 = 0
c5 = 0
c6 = 0
c7 = 0
c8 = 0
c9 = 0
no_of_moves = 0

xclick = 0
yclick = 0

x = grid.xcor()
y = grid.ycor()

r1 = [c1, c4, c7]
r2 = [c2, c5, c8]
r3 = [c3, c6, c9]
d1 = [r1[0], r2[1], r3[2]]
d2 = [r1[2], r2[1], r3[0]]
matrix = [r1, r2, r3]


def update_matrices():
    global r1, r2, r3, d1, d2, matrix
    r1, r2, r3, d1, d2, matrix = [c1, c4, c7], [c2, c5, c8], [c3, c6, c9], [r1[0], r2[1], r3[2]], [r1[2], r2[1],
                                                                                                   r3[0]], [r1, r2, r3]


def win():
    global p_cross, p_circle
    for index in matrix:
        if sum(index) == 3:
            p_cross = 1
        elif sum(index) == -3:
            p_circle = 1
    for vert in map(sum, zip(r1, r2, r3)):
        if vert == 3:
            p_cross = 1
        elif vert == -3:
            p_circle = 1
    if sum(d1) or sum(d2) == 3:
        p_cross = 1
    elif sum(d1) or sum(d2) == -3:
        p_circle = 1
    print(c1, c2, c3, c4, c5, c6, c7, c8, c9)
    print(r1,r2,r3)
    print(p_cross,p_circle)


def cross(x, y):
    global no_of_moves, shape
    grid.goto(x, y)
    grid.pendown()
    grid.goto(x + 200, y + 200)
    grid.goto(x, y + 200)
    grid.goto(x + 200, y)
    grid.penup()
    no_of_moves += 1
    if shape == 0:
        shape = 1
    else:
        shape = 0
    update_matrices()
    win()


def circle(x, y):
    global no_of_moves, shape
    grid.goto(x, y)
    grid.pendown()
    grid.circle(100)
    grid.penup()
    no_of_moves += 1
    if shape == 0:
        shape = 1
    else:
        shape = 0
    update_matrices()
    win()


def modifyglobalvariables(rawx, rawy):
    global xclick
    global yclick
    xclick = int(rawx // 1)
    yclick = int(rawy // 1)

    global shape
    if shape == 1:
        def make_cross(xclick, yclick):
            global c1, c2, c3, c4, c5, c6, c7, c8, c9
            if -300 < xclick < -100 and 100 < yclick < 300 and c1 == 0:
                c1 = 1
                cross(-300, 100)

            if -300 < xclick < -100 and -100 < yclick < 100 and c2 == 0:
                c2 = 1
                cross(-300, -100)

            if -300 < xclick < -100 and -300 < yclick < -100 and c3 == 0:
                c3 = 1
                cross(-300, -300)

            if -100 < xclick < 100 and 100 < yclick < 300 and c4 == 0:
                c4 = 1
                cross(-100, 100)

            if -100 < xclick < 100 and -100 < yclick < 100 and c5 == 0:
                c5 = 1
                cross(-100, -100)

            if -100 < xclick < 100 and -300 < yclick < -100 and c6 == 0:
                c6 = 1
                cross(-100, -300)

            if 100 < xclick < 300 and 100 < yclick < 300 and c7 == 0:
                c7 = 1
                cross(100, 100)

            if 100 < xclick < 300 and -100 < yclick < 100 and c8 == 0:
                c8 = 1
                cross(100, -100)

            if 100 < xclick < 300 and -300 < yclick < -100 and c9 == 0:
                c9 = 1
                cross(100, -300)

        return make_cross(xclick, yclick)
    else:
        def make_circle(xclick, yclick):
            global c1, c2, c3, c4, c5, c6, c7, c8, c9
            if -300 < xclick < -100 and 100 < yclick < 300 and c1 == 0:
                c1 = -1
                circle(-200, 100)

            if -300 < xclick < -100 and -100 < yclick < 100 and c2 == 0:
                c2 = -1
                circle(-200, -100)

            if -300 < xclick < -100 and -300 < yclick < -100 and c3 == 0:
                c3 = -1
                circle(-200, -300)

            if -100 < xclick < 100 and 100 < yclick < 300 and c4 == 0:
                c4 = -1
                circle(0, 100)

            if -100 < xclick < 100 and -100 < yclick < 100 and c5 == 0:
                c5 = -1
                circle(0, -100)

            if -100 < xclick < 100 and -300 < yclick < -100 and c6 == 0:
                c6 = -1
                circle(0, -300)

            if 100 < xclick < 300 and 100 < yclick < 300 and c7 == 0:
                c7 = -1
                circle(200, 100)

            if 100 < xclick < 300 and -100 < yclick < 100 and c8 == 0:
                c8 = -1
                circle(200, -100)

            if 100 < xclick < 300 and -300 < yclick < -100 and c9 == 0:
                c9 = -1
                circle(200, -300)

        return make_circle(xclick, yclick)



wn.onscreenclick(modifyglobalvariables)
wn.mainloop()
