from turtle import Turtle


class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color('#94d2bd')
        self.setpos(0, -250)
        self.shape("square")
        self.shapesize(1, 10)
        self.x_boundary = 450  # Edge of screen

    def move_right(self):
        if self.pos()[0] <= self.x_boundary - 100:  # Check paddle hasn't reached edge of screen.
            self.forward(40)

    def move_left(self):
        if self.pos()[0] >= -self.x_boundary + 90:
            self.backward(40)

    def reset_paddle(self):
        self.setpos(0, -250)