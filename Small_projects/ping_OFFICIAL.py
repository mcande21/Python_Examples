# Ping is my final project video game
# Its going to bounce a tennis ball around with a paddle and a block in the center
# The ball is going to start in a random position CHECK
# The ball is going to have a random velocity CHECK
# This will support mouse movement to control the paddles CHECK
# And there's going to be a big block in the center the ball will bounce against

import random
import color
import pygame
import pygame_helper

pygame.init()
# tell pygame to repeat keydown events
pygame.key.set_repeat(1, 10)

side = 600
win = pygame.display.set_mode((side, side))

win.fill(color.black)

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

    # Check to see if we hit the box at all
    if  rect_x - ball_width < x < rect_x + rect_width and \
            rect_y < y + ball_height < rect_y + rect_height + ball_height:
       wy = (ball_width + rect_width) * ((ball_y + (ball_height // 2)) - (rect_y + (rect_height // 2)))
       hx = (ball_height + rect_height) * ((ball_x + (ball_width // 2)) - (rect_x + (rect_width // 2)))
       if wy > hx:
           # bottom
           if wy > -hx:
               y = rect_y + rect_height
               dy = -dy
            # Left side
           else:
               x = rect_x - ball_width
               dx = -dx
       else:
           # right side
            if wy > -hx:
                x = rect_x + rect_width
                dx = -dx
            # top
            else:
                y = rect_y - ball_height
                dy = -dy
# make sure the ball bounces off the ceiling
    if y < 0:
        y = 0
        dy = -dy
# make sure the ball bounces off the floor
    elif y + ball_height >= side:
        y = side - ball_height
        dy = -dy

    return (x, y, dx, dy)

# MAINE PROGRAM

# load an image file with pygame
ball = pygame.image.load("ball.png").convert_alpha()

# get the width and height of the ball
ball_width = ball.get_width()
ball_height = ball.get_height()
ball_x = random.randrange(side)
ball_y = random.randrange(side)

# initial velocity RANDOM (px/s)
ball_dx = random.randrange(side)
ball_dy = random.randrange(side)

# load the image of the paddle
paddle = pygame.image.load("paddle.png").convert_alpha()
paddle_width = paddle.get_width()
paddle_height = paddle.get_height()

# the paddle will always be 10 pixels from the left side of the window
paddle_x = 10
paddle_y = side // 2 - paddle_height // 2

# create a pygame "stopwatch" object
clock = pygame.time.Clock()

# loop for animation
while True:
    # erase the window
    win.fill(color.black)
    # Draw a rectangle
    rect_width = side // 4
    rect_height = rect_width
    rect_x = (side // 2) - (rect_width // 2)
    rect_y = (side // 2) - (rect_width // 2)
    pygame.draw.rect(win, color.white, (rect_x, rect_y, rect_width, rect_height))

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
        elif event.type == pygame.MOUSEMOTION:
            # The mouse was moved
            # we have to get the position and set the position of the paddle to y position of mouse
            pos = pygame.mouse.get_pos()
            paddle_y = pos[1]

    # check the amount of time since the last iteration
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