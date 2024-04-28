from brick import Brick
import numpy as np
import random
import math

row_y = [0, 30, 60, 90, 120, 150, 180, 210, 240, 270, 300]


class BrickGenerator:
    def __init__(self, num_rows, num_bricks, sector_divisions):
        self.num_rows = num_rows
        self.num_bricks = num_bricks
        self.window_boundary = 450
        self.sector_divisions = sector_divisions
        self.bricks_in_sector = {}
        self.setup_sectors()

    def setup_sectors(self):
        for i in range(-1, self.sector_divisions + 1):
            for j in range(-1, self.sector_divisions + 1):
                self.bricks_in_sector[(i, j)] = []

    def generate_bricks(self):
        for row_number in range(0, self.num_rows):
            bricks_in_row = self.num_bricks + row_number * 3  # Calculate number of bricks for each row
            bricks_x = np.linspace(-self.window_boundary + 10, self.window_boundary - 10, bricks_in_row)
            brick_width = (self.window_boundary * 2) // bricks_in_row - 5  # subtract 10 to create a gap between bricks
            stretch_factor = brick_width / 20

            # Create all the bricks in current row
            for j in range(0, bricks_in_row - 1):
                power = random.randint(0, 200)
                is_big, is_multi_3, is_multi_5 = False, False, False
                if power == 200:
                    is_multi_5 = True
                elif power >= 198:
                    is_multi_3 = True
                elif power >= 195:
                    is_big = True

                # Find which sector the brick is inside
                sector_x = math.floor((bricks_x[j] + 450) * self.sector_divisions/900)
                sector_y = math.floor((row_y[row_number] + 325) * self.sector_divisions/900)

                new_brick = Brick(row_number, (bricks_x[j] + brick_width / 2), row_y[row_number], stretch_factor, is_big, is_multi_3, is_multi_5)
                self.bricks_in_sector[(sector_x, sector_y)].append(new_brick)

    def clear_bricks(self):
        for brick_list in self.bricks_in_sector.values():
            for brick in brick_list:
                brick.hideturtle()

    def next_level(self):
        if self.num_rows < 8:
            self.num_rows += 1
        elif self.num_bricks < 14:
            self.num_bricks += 3
        self.generate_bricks()
