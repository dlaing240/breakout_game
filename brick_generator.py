from brick import Brick
import numpy as np
import random

row_y = [0, 30, 60, 90, 120, 150, 180, 210, 240, 270, 300]


class BrickGenerator:
    def __init__(self, num_rows, num_bricks):
        self.num_rows = num_rows
        self.num_bricks = num_bricks
        self.brick_list = []
        self.window_boundary = 450

    def generate_bricks(self):
        for row_number in range(0, self.num_rows):
            bricks_in_row = self.num_bricks + row_number * 3  # Calculate number of bricks for each row
            bricks_x = np.linspace(-self.window_boundary + 10, self.window_boundary - 10, bricks_in_row)
            brick_width = (self.window_boundary * 2) // bricks_in_row - 10  # subtract 10 to create a gap between bricks
            stretch_factor = brick_width / 20

            # Create all the bricks in current row
            for j in range(0, bricks_in_row-1):
                power = random.randint(0, 100)
                is_big, is_multi_3, is_multi_5 = False, False, False
                if power == 100:
                    is_multi_5 = True
                elif power >= 98:
                    is_multi_3 = True
                elif power >= 95:
                    is_big = True

                self.brick_list.append(Brick
                    (
                    row=row_number,
                    brick_x=(bricks_x[j] + brick_width/2),
                    brick_y=row_y[row_number],
                    brick_width=stretch_factor,
                    is_big=is_big,
                    is_multi_3=is_multi_3,
                    is_multi_5=is_multi_5
                    )
                )

    def clear_bricks(self):
        for brick in self.brick_list:
            brick.hideturtle()

    def next_level(self):
        if self.num_rows < 8:
            self.num_rows += 1
        elif self.num_bricks < 20:
            self.num_bricks += 3
        self.generate_bricks()
