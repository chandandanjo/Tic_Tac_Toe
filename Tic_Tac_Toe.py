import ctypes
import turtle
# import random
# import time
import numpy as np

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

x_click = 0
y_click = 0


matrix = np.array([[c1, c4, c7], [c2, c5, c8], [c3, c6, c9]])
vert = matrix.sum(axis=0)
hor = matrix.sum(axis=1)
d1 = np.trace(matrix)
d2 = np.fliplr(matrix).trace()


def win():
    global p_cross, p_circle
    for index in vert:
        if index == 3:
            p_cross = 1
        elif index == -3:
            p_circle = 1
    for index in hor:
        if index == 3:
            p_cross = 1
        elif index == -3:
            p_circle = 1
    if d1 == 3 or d2 == 3:
        p_cross = 1
    elif d1 == -3 or d2 == -3:
        p_circle = 1


def update_matrices():
    global matrix, vert, hor, d1, d2
    matrix = np.array([[c1, c4, c7], [c2, c5, c8], [c3, c6, c9]])
    vert = matrix.sum(axis=0)
    hor = matrix.sum(axis=1)
    d1 = np.trace(matrix)
    d2 = np.fliplr(matrix).trace()


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


def modify_global_variables(raw_x, raw_y):
    global x_click
    global y_click
    x_click = int(raw_x // 1)
    y_click = int(raw_y // 1)

    global shape
    if shape == 1 and p_cross == 0 and p_circle == 0:

        def make_cross():
            global c1, c2, c3, c4, c5, c6, c7, c8, c9
            if -300 < x_click < -100 and 100 < y_click < 300 and c1 == 0:
                c1 = 1
                cross(-300, 100)

            if -300 < x_click < -100 and -100 < y_click < 100 and c2 == 0:
                c2 = 1
                cross(-300, -100)

            if -300 < x_click < -100 and -300 < y_click < -100 and c3 == 0:
                c3 = 1
                cross(-300, -300)

            if -100 < x_click < 100 and 100 < y_click < 300 and c4 == 0:
                c4 = 1
                cross(-100, 100)

            if -100 < x_click < 100 and -100 < y_click < 100 and c5 == 0:
                c5 = 1
                cross(-100, -100)

            if -100 < x_click < 100 and -300 < y_click < -100 and c6 == 0:
                c6 = 1
                cross(-100, -300)

            if 100 < x_click < 300 and 100 < y_click < 300 and c7 == 0:
                c7 = 1
                cross(100, 100)

            if 100 < x_click < 300 and -100 < y_click < 100 and c8 == 0:
                c8 = 1
                cross(100, -100)

            if 100 < x_click < 300 and -300 < y_click < -100 and c9 == 0:
                c9 = 1
                cross(100, -300)

        return make_cross()
    elif shape == 0 and p_cross == 0 and p_circle == 0:

        def make_circle():
            global c1, c2, c3, c4, c5, c6, c7, c8, c9
            if -300 < x_click < -100 and 100 < y_click < 300 and c1 == 0:
                c1 = -1
                circle(-200, 100)

            if -300 < x_click < -100 and -100 < y_click < 100 and c2 == 0:
                c2 = -1
                circle(-200, -100)

            if -300 < x_click < -100 and -300 < y_click < -100 and c3 == 0:
                c3 = -1
                circle(-200, -300)

            if -100 < x_click < 100 and 100 < y_click < 300 and c4 == 0:
                c4 = -1
                circle(0, 100)

            if -100 < x_click < 100 and -100 < y_click < 100 and c5 == 0:
                c5 = -1
                circle(0, -100)

            if -100 < x_click < 100 and -300 < y_click < -100 and c6 == 0:
                c6 = -1
                circle(0, -300)

            if 100 < x_click < 300 and 100 < y_click < 300 and c7 == 0:
                c7 = -1
                circle(200, 100)

            if 100 < x_click < 300 and -100 < y_click < 100 and c8 == 0:
                c8 = -1
                circle(200, -100)

            if 100 < x_click < 300 and -300 < y_click < -100 and c9 == 0:
                c9 = -1
                circle(200, -300)

        return make_circle()
    else:
        wn.reset()
        message_box = ctypes.windll.user32.MessageBoxW
        if p_cross == 1:
            message_box(None, 'Player cross', 'Match Winner', 0)
        if p_circle == 1:
            message_box(None, 'Player circle', 'Match Winner', 0)


wn.onscreenclick(modify_global_variables)
wn.mainloop()
