from turtle import Turtle


colours = ["#f94144", "#f3722c", "#f8961e", "#f9c74f", "#90be6d", "#43aa8b", "#5d5790", "#84358c", ]
powerup_colours = ["#f878ff", "#26ff00", "#0400ff"]


class Brick(Turtle):
    def __init__(self, row, brick_x, brick_y, brick_width, is_big, is_multi_3, is_multi_5):
        super().__init__()
        self.row = row
        self.value = (row + 1) * 5

        self.color(colours[row])

        if is_big:
            self.color(powerup_colours[0])
        elif is_multi_3:
            self.color(powerup_colours[1])
        elif is_multi_5:
            self.color(powerup_colours[2])

        self.penup()
        self.shape("square")
        self.shapesize(1, brick_width)
        self.setx(brick_x)
        self.sety(brick_y)

        self.brick_y = brick_y
        self.brick_left = brick_x - brick_width*10
        self.brick_right = brick_x + brick_width*10
        self.brick_top = brick_y + 10
        self.brick_bottom = brick_y - 10

        # Powerups
        self.is_big = is_big
        self.is_multi_3 = is_multi_3
        self.is_multi_5 = is_multi_5
