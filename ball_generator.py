from ball import Ball
import random


class BallGenerator:
    def __init__(self):
        self.ball_list = []
        self.ball_speed = 10.5

    def generate_balls(self, ball_num):
        for i in range(0, ball_num):
            self.ball_list.append(Ball(ball_speed=self.ball_speed))

    def move_balls(self):
        for ball in self.ball_list:
            ball.move()

    def get_ball_pos(self):
        positions = []
        for ball in self.ball_list:
            positions.append(ball.pos())
        return positions

    def generate_big_ball(self):
        big_ball = Ball(self.ball_speed)
        big_ball.shapesize(3, 3)
        big_ball.ball_width = 30
        self.ball_list.append(big_ball)

    def generate_multi_ball(self, num):
        for i in range(0, num):
            new_ball = Ball(self.ball_speed)
            new_ball.setheading(random.randint(75, 115))
            self.ball_list.append(new_ball)

    def next_level(self):
        for ball in self.ball_list:
            ball.hideturtle()
        self.ball_list = []
        self.ball_speed += 0.5
        self.generate_balls(1)
