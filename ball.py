from turtle import Turtle
import random


class Ball(Turtle):
    def __init__(self, ball_speed):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("#e9d8a6")
        self.setpos(0, -230)
        self.setheading(random.randint(80, 110))
        self.ball_speed = ball_speed
        self.ball_width = 10

    def move(self):
        self.forward(self.ball_speed)

    def vertical_bounce(self):  # Used for walls
        self.setheading(180 - self.heading())

    def horizontal_bounce(self):  # Used for ceiling
        self.setheading(360 - self.heading())

    def paddle_bounce(self, hit_point):
        new_heading = 150 - (hit_point + 101) * 60/101
        self.setheading(new_heading)

    def reset_ball(self):
        self.setpos(0, -230)
        self.setheading(85)

