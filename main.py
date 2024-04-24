from turtle import Screen
import time
from paddle import Paddle
from brick_generator import BrickGenerator
from ball_generator import BallGenerator
from scoreboard import Scoreboard


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
brick_generator = BrickGenerator(2, 8)
brick_generator.generate_bricks()
ball_generator = BallGenerator()
ball_generator.generate_balls(1)
scoreboard = Scoreboard()

# Game procedure
gaming = True
while gaming:

    # End level condition: all bricks have been broken
    if not brick_generator.brick_list:
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
    ball_positions = ball_generator.get_ball_pos()

    # Check each ball for interactions
    for ball in ball_generator.ball_list:
        ball_pos = ball.pos()

        # Out of bounds
        if ball_pos[1] - ball.ball_width <= floor:
            ball.hideturtle()
            ball_generator.ball_list.remove(ball)
            continue

        # Collision with walls
        if ball_pos[0] + ball.ball_width >= right_wall or ball_pos[0] - ball.ball_width <= left_wall:
            ball.vertical_bounce()
            continue

        # Collision with ceiling
        if ball_pos[1] + ball.ball_width >= ceiling:
            ball.horizontal_bounce()
            # Fail-safe to prevent ball getting stuck on the ceiling
            if ball_pos[1] >= ceiling - 5:
                ball.sety(ceiling - ball.ball_width)
            continue

        # Collision with paddle
        paddle_pos = paddle.pos()
        if abs(ball_pos[0] - paddle_pos[0]) < (100 + ball.ball_width) and abs(ball_pos[1] - paddle_pos[1]) < (15 + ball.ball_width):
            hit_point = ball_pos[0] - paddle_pos[0]
            ball.paddle_bounce(hit_point)
            continue

        # Collisions with bricks
        for brick in brick_generator.brick_list:
            if ((brick.brick_left - ball.ball_width) <= ball_pos[0] <= (brick.brick_right + ball.ball_width)
                    and (brick.brick_bottom - 5 - ball.ball_width) <= ball_pos[1] <= (brick.brick_top + 5 + ball.ball_width)):
                if brick.brick_left <= ball_pos[0] <= brick.brick_right:
                    ball.horizontal_bounce()
                    brick.hideturtle()
                    brick_generator.brick_list.remove(brick)
                    scoreboard.increase_score(brick.value)
                else:
                    ball.vertical_bounce()
                    brick.hideturtle()
                    brick_generator.brick_list.remove(brick)
                    scoreboard.increase_score(brick.value)

                # Check for powerups
                if brick.is_big:
                    ball_generator.generate_big_ball()
                elif brick.is_multi_3:
                    ball_generator.generate_multi_ball(3)
                elif brick.is_multi_5:
                    ball_generator.generate_multi_ball(5)

    time.sleep(0.02)
    screen.update()

screen.exitonclick()
