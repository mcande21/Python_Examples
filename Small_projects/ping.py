# Ping is a version of the classic pong arcade game
# bounce a tenis ball off the wall and dont miss

import random

import color
import pygame
import pygame_helper

def move(x, y, dx, dy, dt):
    """
    A function that moves a ball based on a starting location and velocity
    :param x: initial x-coordinate
    :param y: initial y - coordinate
    :param dx: horizontal velocity
    :param dy: vertical velocity
    :param dt: time elapsed
    :return: (x, y, dx, dy) of the update location and velocity
    """
    x = x + dx * dt
    y = y + dy * dt

    # check if we hit the paddle or the right side wall
    if x < paddle_x + paddle_width and paddle_y <= y + ball_height // 2 <= paddle_y + paddle_height:
        x = paddle_x + paddle_width
        dx = -dx
    elif x + ball_width >= side:
        x = side - ball_width
        dx = -dx

    if y < 0:
        y = 0
        dy = -dy
    elif y + ball_height >= side:
        y = side - ball_height
        dy = -dy

    return (x, y, dx, dy)


pygame.init()
# tell pygame to repeat keydown events
pygame.key.set_repeat(1, 10)

side = 600
win = pygame.display.set_mode((side, side))

win.fill(color.black)

# load an image file with pygame
ball = pygame.image.load("ball.png").convert_alpha()
# get width returns the number of pixels wide for the surface
ball_width = ball.get_width()
ball_height = ball.get_height()
ball_x = side // 2 - ball_width // 2
ball_y = side // 2 - ball_height // 2

# initial velocity (px/s)
ball_dx = side // 3
ball_dy = side // 2

# load the image of the paddle
paddle = pygame.image.load("paddle.png").convert_alpha()
paddle_width = paddle.get_width()
paddle_height = paddle.get_height()

# the paddle will always be 10 pixels from the left side of the window
paddle_x = 10
paddle_y = side // 2 - paddle_height // 2

# how far should the paddle move?
# the paddle will move 8 pixels at a time up and down
paddle_dy = 8
# create a pygame "stopwatch" object
clock = pygame.time.Clock()
# loop for animation
while True:
    # erase the window
    win.fill(color.black)
    # check to see if we lost
    if ball_x < 0:
        exit()
    # process all the events
    for event in pygame.event.get():
        # check the type of the event
        if event.type == pygame.QUIT:
            # the user clicked the x quit at the top right of the window
            # python has a function called exit that will quite the program
            exit()
        elif event.type == pygame.KEYDOWN:
            # a keyboard button was pressed
            if event.key == pygame.K_DOWN:
                # the down key pressed, move the paddle down
                paddle_y += paddle_dy
            elif event.key == pygame.K_UP:
                # move the paddle up
                paddle_y -= paddle_dy

    # check the amount of time since the last iteration
    # tick tells us how many milliseconds have elapsed since the last tie we called the function
    # divide by 1000 we get seconds
    # 60 limits the animation frame rate to 60 fps
    time_elapsed = clock.tick(60) / 1000

    # move the ball
    ball_x, ball_y, ball_dx, ball_dy = move(ball_x, ball_y, ball_dx, ball_dy, time_elapsed)

    # check that the paddle is still in the bounds of the window.
    if paddle_y < 0:
        # went too far up
        paddle_y = 0
    elif paddle_y + paddle_height >= side:
        # went too far down
        paddle_y = side - paddle_height

    # draw the ball and paddle
    win.blit(ball, (ball_x, ball_y))
    win.blit(paddle, (paddle_x, paddle_y))

    # update the screen
    pygame.display.update()


win.blit(ball, (ball_x, ball_y))

pygame.display.update()
pygame_helper.wait_for_click()