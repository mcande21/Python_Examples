# This program is going to draw a super creative and fun beautiful house!!
# Its going to be a lot but im excited!

# importing everything
import pygame
import pygame.display

import pygame_helper
import color

# let pygame prepare our program for graphics
pygame.init()

# Set the dimensions of the window
width = 800
height = 600

# create a program window
win = pygame.display.set_mode((width, height))

# fill the window with a color
win.fill(color.lightgray)

def window_func(w_width, w_height, w_x, w_y):
    """
    This program will draw a window with an outline and lines crossing thie window
    :param w_width: The input width of the window
    :param w_height: the input height of the window
    :param w_x: the x position
    :param w_y: the y position
    :return: The side effects of window with some lines in it
    """
    # first I have to define the window and its variables
    pygame.draw.rect(win, color.lightgray, (w_x, w_y, w_width, w_height))
    # drawing some lines across it
    pygame.draw.line(win, color.black, (w_x + w_width // 2, w_y), (w_x + w_width // 2, w_y + w_height), 2)
    pygame.draw.line(win, color.black, (w_x, w_y + w_height // 2), (w_x + w_width, w_y + w_height // 2), 2)

    return None

# creating the basics of the house: rectangles R1 and R2
R1_width = (width * 4) // 10
R1_height = (height * 6.5) // 10
R1_x = width // 2 - R1_width * 1.15
R1_y = height - R1_height
pygame.draw.rect(win, color.almost_black, (R1_x, R1_y, R1_width, R1_height))

R2_width = R1_width * 5.5 // 10
R2_height = R1_height * 4.75 // 10
R2_x = R1_x + R1_width
R2_y= height - R2_height
pygame.draw. rect(win, color.almost_black, (R2_x, R2_y, R2_width, R2_height))

# creating the roofs that will go on R1 and R2
r1_width = R1_width * 14 // 10
r1_height = R1_height * 1 // 20
r1_x = R1_x
r1_y = R1_y - r1_height
pygame.draw.rect(win, color.black, (r1_x, r1_y, r1_width, r1_height))

r2_width = R2_width * 22.15 // 10
r2_height = R2_height * 1 // 20
r2_x = R2_x
r2_y = R2_y - r2_height
pygame.draw.rect(win, color.black, (r2_x, r2_y, r2_width, r2_height))

# creating the pillar
p1_width = R1_width * 1 // 20
p1_height = R2_height
p1_x = R2_x + 2 * R2_width
p1_y = R2_y
pygame.draw.rect(win, color.burntsienna_but_brown, (p1_x, p1_y, p1_width, p1_height))

# creating the railing
rail_width = R2_width * 22 // 10
rail_height = R2_height * 1 // 20
rail_x = r2_x
rail_y = r2_y - R2_y * 1.5 // 10
pygame.draw.rect(win, color.burntsienna_but_brown, (rail_x, rail_y, rail_width, rail_height))

# drawing the railing bars
RB_x = rail_width

# This while loop will draw out the railing bars under my railing
while RB_x < rail_x + rail_width:
    # drawing one railing, farthest to the left
    pygame.draw.line(win, color.light_burntsienna, (RB_x, rail_y), (RB_x, r2_y), int(rail_width // 50))
    # moving the railing to the right a value until it reaches the limit
    RB_x = RB_x + rail_width // 11

# drawing windows using function
w1_width = R1_width * 2 // 10
w1_height = R1_height * 3 // 10
w1_x = R1_x + R1_width * 2.5 // 20
w1_y = R1_y + R1_height * 2 // 20
window_func(w1_width, w1_height, w1_x, w1_y)

w2_width = R1_width * 5.35 // 10
w2_height = R1_height * 2 // 10
w2_x = R1_x + R1_width * 9 // 20
w2_y = R1_y + R1_height * 2 // 20
window_func(w2_width, w2_height, w2_x, w2_y)

w3_width = R1_width * 6 // 10
w3_height = R1_height * 2.25 // 10
w3_x = R1_x + R1_width * 18 // 20
w3_y = R1_y + R1_height * 12.5 // 20
window_func(w3_width, w3_height, w3_x, w3_y)

w4_width = R1_width * 2 // 10
w4_height = R1_height * 3 // 10
w4_x = R1_x + R1_width * 11 // 20
w4_y = R1_y + R1_height * 12.25 // 20
window_func(w4_width, w4_height, w4_x, w4_y)

# drawing the door
d_width = R1_width * 2.4 // 10
d_height = R1_height * 4 // 10
d_x = R1_x + R1_width * 3 // 20
d_y = R1_y + R1_height * 6 // 10
pygame.draw.rect(win, color.darker_grey, (d_x, d_y, d_width, d_height))

# drawing the door knob
c_radius = d_width * 1.5 // 20
c_x = d_x + d_width * 8.25 // 10
c_y = d_y + d_height * 5.75 // 10
pygame.draw.circle(win, color.black, (c_x, c_y), c_radius)

# building the lights in the window
# this is one light I will put in a while function
# using i to hold a spot
side = w2_height * 1 // 10
l1_x = w2_x + w2_width // 6 - side // 2
light_p = w2_x + w2_width // 6

while light_p < w2_x + w2_width:
    # drawing the initial light
    pygame.draw.line(win, color.darker_grey, (light_p, w2_y), (light_p, w2_y + w2_height * 3 // 10), 2)

    side = w2_height * 1 // 10
    l1_x = light_p - side // 2
    l1_y = w2_y + w2_height * 3 // 10
    pygame.draw.rect(win, color.warm_yellow, (l1_x, l1_y, side, side))
    # then were going to move the light to the right
    light_p = light_p + w2_width // 4.5
    pygame.display.update()

side2 = w3_height * 1 // 10
l1_x2 = w3_x + w3_width // 6 - side // 2
light_p2 = w3_x + w3_width // 6

while light_p2 < w3_x + w3_width:
    # drawing the initial light
    pygame.draw.line(win, color.black, (light_p2, w3_y), (light_p2, w3_y + w3_height * 3 // 10), 2)

    side = w3_height * 1 // 10
    l2_x = light_p2 - side // 2
    l2_y = w3_y + w3_height * 3 // 10
    pygame.draw.rect(win, color.warm_yellow, (l2_x, l2_y, side, side))
    # then were going to move the light to the right
    light_p2 = light_p2 + w3_width // 4.5
    pygame.display.update()


# finally updating the program
pygame.display.update()
# and finally waiting for that damn click
pygame_helper.wait_for_click()