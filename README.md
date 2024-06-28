# Breakout Clone

A simple game made in Python using turtle graphics, based on the arcade game 'Breakout'. 

## Requirements

- Python
- NumPy


## Description
![Screenshot 1_crop](https://github.com/dlaing240/breakout_game/assets/159714200/3f3acdd2-344d-435f-92b5-7fa3e743911d)

The game features a ball, a player-controlled paddle and layers of bricks. The bricks are destroyed when the ball collides with them. Progression to the next level occurs once all bricks have been broken. The number of rows and bricks increases through the levels, up to a point.

![level-progression](https://github.com/dlaing240/breakout_game/assets/159714200/908673df-92db-4c0b-a5e0-fea994502051)

### Powerups:
![Powerups](https://github.com/dlaing240/breakout_game/assets/159714200/c62fe36f-fdf3-4e53-bd3f-f8d69f2347bc)

The bricks are generated at the start of each level. Each brick has a small chance to be one of the three powerups: a 'big ball' powerup that generates a larger ball, and two 'multi-ball' powerups that generate 3 or 5 balls at once. These bricks are brightly coloured to make them stand out from the rest of the bricks. The chance for these power-up bricks is low. The score increases with every broken brick, where the amount of points gained depends on which row the brick was a part of.

### Game Over
![game-over screen_cropped](https://github.com/dlaing240/breakout_game/assets/159714200/32bd3739-f978-42b5-8c03-01d5d66ac8d2)


There is a 'lives' system. Lives are lost whenever there are no balls left on the screen, at which point a new ball is generated, and the game ends when the player runs out of lives. The player starts with a generous 10 lives, as this was just enough to allow me to test the later levels.

### Performance

The game uses a simple implementation of spatial partitioning; the space is split into a grid, and each brick is mapped to the section of the grid it is located within. During gameplay, only the bricks that are located in sectors near the ball are included in the calculation, improving performance. However, this isn't very significant in this instance, since the limit on performance comes from using the turtle graphics module, so the game still runs slower at large numbers of bricks. This gives the player additional motivation to destroy the bricks, but it also makes the experience less fun and therefore there is a limit imposed on the number of bricks.
