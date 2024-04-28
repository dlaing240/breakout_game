from turtle import Screen
import time
from paddle import Paddle
from brick_generator import BrickGenerator
from ball_generator import BallGenerator
from scoreboard import Scoreboard
import math


def get_sector(x, y):
    sector_x = math.floor((x + 450) * 8/900)
    sector_y = math.floor((y + 325) * 8/900)
    return sector_x, sector_y


def locate_ball_sector(ball_position):
    x_pos = [ball_position[0] - 100, ball_position[0], ball_position[0] + 100]  # Include adjacent sectors if the ball is close to them
    y_pos = [ball_position[1] - 100, ball_position[1], ball_position[1] + 100]
    sectors = set()
    for x in x_pos:
        for y in y_pos:
            sectors.add(get_sector(x, y))
    return sectors


# Setup screen
screen = Screen()
screen.setup(900, 650)
screen.bgcolor('#001219')
# Turn animations off
screen.tracer(0)
screen.listen()

# boundary coordinates
left_wall = -440
right_wall = 450
ceiling = 315
floor = -320

# Create game objects
paddle = Paddle()
screen.onkeypress(fun=paddle.move_right, key='Right')
screen.onkeypress(fun=paddle.move_left, key='Left')
brick_generator = BrickGenerator(num_rows=2, num_bricks=8, sector_divisions=8)
brick_generator.generate_bricks()
ball_generator = BallGenerator()
ball_generator.generate_balls(1)
scoreboard = Scoreboard()

# Game procedure
gaming = True
while gaming:

    # End level condition: all bricks have been broken
    if all(not values for values in brick_generator.bricks_in_sector.values()):
        ball_generator.next_level()
        paddle.reset_paddle()
        brick_generator.next_level()
        scoreboard.increase_level()
        screen.update()
        time.sleep(1)

    # Game over condition: There are no balls left on screen
    if not ball_generator.ball_list:
        scoreboard.lives -= 1
        if scoreboard.lives > 0:
            time.sleep(0.3)
            ball_generator.generate_balls(1)
            paddle.reset_paddle()
            scoreboard.update_score()
            screen.update()
            time.sleep(0.6)
        # Game ends if there are no lives left
        else:
            paddle.hideturtle()
            brick_generator.clear_bricks()
            screen.update()
            scoreboard.game_over_screen()
            # End the while loop condition
            gaming = False
            break

    # Provide ball motion
    ball_generator.move_balls()
    paddle_pos = paddle.pos()

    # Check each ball for interactions
    for ball in ball_generator.ball_list:
        ball_pos = ball.pos()
        ball_sectors = locate_ball_sector(ball_pos)

        # Out of bounds
        if ball_pos[1] - ball.ball_width <= floor:
            ball.hideturtle()
            ball_generator.ball_list.remove(ball)
            continue

        # Collision with walls
        if ball_pos[0] + ball.ball_width >= right_wall or ball_pos[0] - ball.ball_width <= left_wall:
            ball.vertical_bounce()
            # Fail-safe in case ball gets stuck outside the wall
            if ball_pos[0] + ball.ball_width >= right_wall + 5:
                ball.setx(right_wall - ball.ball_width - 1)
            if ball_pos[0] - ball.ball_width <= left_wall - 5:
                ball.setx(left_wall + ball.ball_width + 1)
            continue

        # Collision with ceiling
        if ball_pos[1] + ball.ball_width >= ceiling:
            ball.horizontal_bounce()
            # Fail-safe to prevent ball getting stuck on the ceiling
            if ball_pos[1] + ball.ball_width >= ceiling + 5:
                ball.sety(ceiling - ball.ball_width - 1)
            continue

        # Collision with paddle
        if abs(ball_pos[0] - paddle_pos[0]) < (100 + ball.ball_width) and abs(ball_pos[1] - paddle_pos[1]) < (15 + ball.ball_width):
            hit_point = ball_pos[0] - paddle_pos[0]
            ball.paddle_bounce(hit_point)
            continue

        # Collisions with bricks
        for sector in ball_sectors:
            for brick in brick_generator.bricks_in_sector[sector]:
                if ((brick.brick_left - ball.ball_width) <= ball_pos[0] <= (brick.brick_right + ball.ball_width)
                        and (brick.brick_bottom - ball.ball_width) <= ball_pos[1] <= (
                                brick.brick_top + ball.ball_width)):
                    if brick.brick_left <= ball_pos[0] <= brick.brick_right:
                        ball.horizontal_bounce()
                        brick.hideturtle()
                        brick_generator.bricks_in_sector[sector].remove(brick)
                        scoreboard.increase_score(brick.value)
                    else:
                        ball.vertical_bounce()
                        brick.hideturtle()
                        brick_generator.bricks_in_sector[sector].remove(brick)
                        scoreboard.increase_score(brick.value)

                    # Check for powerups
                    if brick.is_big:
                        ball_generator.generate_big_ball()
                    elif brick.is_multi_3:
                        ball_generator.generate_multi_ball(3)
                    elif brick.is_multi_5:
                        ball_generator.generate_multi_ball(5)

    time.sleep(0.02)  # This is needed to prevent game from rapidly speeding up as more bricks are broken
    screen.update()

screen.exitonclick()
