import ctypes
import turtle
import numpy as np
from pynput.mouse import Button, Controller


class Game:
    def __init__(self):
        self.wn = turtle.Screen()
        self.wn.title("Tic Tac Toe")
        self.wn.setup(width=600, height=600)
        self.wn.bgcolor("Black")
        self.wn.tracer(0)
        self.wn.listen()

        self.grid = turtle.Turtle()
        self.grid.color("White")
        self.grid.speed(0)
        self.grid.pensize(width=5)
        self.grid.penup()

        self.shape = self.wn.numinput("Cross or Circle ?", "For cross enter: 1, For circle enter: 0", minval=0,
                                      maxval=1)
        self.p_cross = 0
        self.p_circle = 0

        self.mouse = Controller()

        self.c1 = 0
        self.c2 = 0
        self.c3 = 0
        self.c4 = 0
        self.c5 = 0
        self.c6 = 0
        self.c7 = 0
        self.c8 = 0
        self.c9 = 0
        self.no_of_moves = 0

        self.x_click = 0
        self.y_click = 0

        self.matrix = np.array([[self.c1, self.c4, self.c7], [self.c2, self.c5, self.c8], [self.c3, self.c6, self.c9]])
        self.vert = self.matrix.sum(axis=0)
        self.hor = self.matrix.sum(axis=1)
        self.d1 = np.trace(self.matrix)
        self.d2 = np.fliplr(self.matrix).trace()

        self.message_box = ctypes.windll.user32.MessageBoxW

    def grid_formation(self):
        self.grid.goto(-300, 300)
        self.grid.pendown()
        for i in range(4):
            self.grid.forward(600)
            self.grid.right(90)
            for j in range(4):
                self.grid.forward(200)
                self.grid.right(90)
        self.grid.penup()
        self.grid.goto(-100, 100)
        self.grid.pendown()
        for k in range(4):
            self.grid.forward(200)
            self.grid.right(90)
        self.grid.penup()

    def cross(self, x, y):
        self.grid.goto(x, y)
        self.grid.pendown()
        self.grid.goto(x + 200, y + 200)
        self.grid.goto(x, y + 200)
        self.grid.goto(x + 200, y)
        self.grid.penup()
        self.no_of_moves += 1
        if self.shape == 0:
            self.shape = 1
        else:
            self.shape = 0
        self.update_matrices()
        self.win()
        self.mouse.click(Button.left, 2)

    def circle(self, x, y):
        self.grid.goto(x, y)
        self.grid.pendown()
        self.grid.circle(100)
        self.grid.penup()
        self.no_of_moves += 1
        if self.shape == 0:
            self.shape = 1
        else:
            self.shape = 0
        self.update_matrices()
        self.win()
        self.mouse.click(Button.left, 2)

    def make_circle(self):
        if -300 < self.x_click < -100 and 100 < self.y_click < 300 and self.c1 == 0:
            self.c1 = -1
            self.circle(-200, 100)

        if -300 < self.x_click < -100 and -100 < self.y_click < 100 and self.c2 == 0:
            self.c2 = -1
            self.circle(-200, -100)

        if -300 < self.x_click < -100 and -300 < self.y_click < -100 and self.c3 == 0:
            self.c3 = -1
            self.circle(-200, -300)

        if -100 < self.x_click < 100 and 100 < self.y_click < 300 and self.c4 == 0:
            self.c4 = -1
            self.circle(0, 100)

        if -100 < self.x_click < 100 and -100 < self.y_click < 100 and self.c5 == 0:
            self.c5 = -1
            self.circle(0, -100)

        if -100 < self.x_click < 100 and -300 < self.y_click < -100 and self.c6 == 0:
            self.c6 = -1
            self.circle(0, -300)

        if 100 < self.x_click < 300 and 100 < self.y_click < 300 and self.c7 == 0:
            self.c7 = -1
            self.circle(200, 100)

        if 100 < self.x_click < 300 and -100 < self.y_click < 100 and self.c8 == 0:
            self.c8 = -1
            self.circle(200, -100)

        if 100 < self.x_click < 300 and -300 < self.y_click < -100 and self.c9 == 0:
            self.c9 = -1
            self.circle(200, -300)

    def make_cross(self):
        if -300 < self.x_click < -100 and 100 < self.y_click < 300 and self.c1 == 0:
            self.c1 = 1
            self.cross(-300, 100)

        if -300 < self.x_click < -100 and -100 < self.y_click < 100 and self.c2 == 0:
            self.c2 = 1
            self.cross(-300, -100)

        if -300 < self.x_click < -100 and -300 < self.y_click < -100 and self.c3 == 0:
            self.c3 = 1
            self.cross(-300, -300)

        if -100 < self.x_click < 100 and 100 < self.y_click < 300 and self.c4 == 0:
            self.c4 = 1
            self.cross(-100, 100)

        if -100 < self.x_click < 100 and -100 < self.y_click < 100 and self.c5 == 0:
            self.c5 = 1
            self.cross(-100, -100)

        if -100 < self.x_click < 100 and -300 < self.y_click < -100 and self.c6 == 0:
            self.c6 = 1
            self.cross(-100, -300)

        if 100 < self.x_click < 300 and 100 < self.y_click < 300 and self.c7 == 0:
            self.c7 = 1
            self.cross(100, 100)

        if 100 < self.x_click < 300 and -100 < self.y_click < 100 and self.c8 == 0:
            self.c8 = 1
            self.cross(100, -100)

        if 100 < self.x_click < 300 and -300 < self.y_click < -100 and self.c9 == 0:
            self.c9 = 1
            self.cross(100, -300)

    def update_matrices(self):
        self.matrix = np.array([[self.c1, self.c4, self.c7], [self.c2, self.c5, self.c8], [self.c3, self.c6, self.c9]])
        self.vert = self.matrix.sum(axis=0)
        self.hor = self.matrix.sum(axis=1)
        self.d1 = np.trace(self.matrix)
        self.d2 = np.fliplr(self.matrix).trace()

    def win(self):
        for index in self.vert:
            if index == 3:
                self.p_cross = 1
            elif index == -3:
                self.p_circle = 1
        for index in self.hor:
            if index == 3:
                self.p_cross = 1
            elif index == -3:
                self.p_circle = 1
        if self.d1 == 3 or self.d2 == 3:
            self.p_cross = 1
        elif self.d1 == -3 or self.d2 == -3:
            self.p_circle = 1

    def score_reset(self):
        self.c1, self.c2, self.c3, self.c4, self.c5, self.c6, self.c7, self.c8, self.c9, self.p_circle, self.p_cross = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
        self.update_matrices()
        self.wn.clearscreen()
        self.wn.bgcolor("black")
        self.wn.tracer(0)
        self.wn.listen()
        self.grid_formation()
        self.grid_formation()
        self.wn.onscreenclick(self.modify_global_variables)

    def match_winner_declaration(self):
        if self.p_cross == 1:
            self.message_box(None, 'Player cross wins!', 'Match Result', 0)
        if self.p_circle == 1:
            self.message_box(None, 'Player circle wins!', 'Match Result', 0)

    def modify_global_variables(self, raw_x, raw_y):
        self.x_click = int(raw_x // 1)
        self.y_click = int(raw_y // 1)

        if self.shape == 1 and self.p_cross == 0 and self.p_circle == 0:
            return self.make_cross()
        elif self.shape == 0 and self.p_cross == 0 and self.p_circle == 0:
            return self.make_circle()
        else:
            self.match_winner_declaration()
            self.score_reset()


tic_tac_toe = Game()

tic_tac_toe.grid_formation()
tic_tac_toe.wn.onscreenclick(tic_tac_toe.modify_global_variables)
tic_tac_toe.wn.mainloop()
